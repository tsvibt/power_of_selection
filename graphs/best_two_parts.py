from matplotlib import pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
import time

#exec(open('graphs/best_two_parts.py').read())
exec(open('stats.py').read())

plt.rcParams["figure.figsize"] = [10, 8]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()

plt.xscale('log')
x_max = 5
x_axis = np.ndarray.astype(10**np.linspace(.4, x_max+.4, 10*x_max) , 'int')


ax.plot(x_axis, [gaussian_max_median(x, 1, 0) for x in x_axis], color='cyan',linestyle='solid', label='median: Φ⁻¹((1/2)^(1/x))')

experiments_count = 70
sample_acc = []
for _ in range(experiments_count):
   samples = [gaussian_max_sample(sample_count, 1, 0) for sample_count in x_axis] 
   sample_acc.append(samples)
   ax.scatter(x_axis, samples, color='green', s=83, alpha=.08, edgecolor='none')

ax.plot(x_axis, [sum(i)/experiments_count for i in zip(*sample_acc)],linestyle='dotted', color='black', label='sample mean')
ax.plot(x_axis, [statistics.median(i) for i in zip(*sample_acc)],linestyle='dashed', color='orange', label='sample median')



ax.plot(x_axis, [2*gaussian_max_median(x, 1/np.sqrt(2), 0) for x in x_axis], color='cyan',linestyle='solid', label='median: Φ⁻¹((1/2)^(1/x))')

experiments_count = 70
sample_acc = []
for _ in range(experiments_count):
   samples = [gaussian_max_sample(sample_count, 1, 0) for sample_count in x_axis] 
   sample_acc.append(samples)
   ax.scatter(x_axis, samples, color='green', s=83, alpha=.08, edgecolor='none')

ax.plot(x_axis, [sum(i)/experiments_count for i in zip(*sample_acc)],linestyle='dotted', color='black', label='sample mean')
ax.plot(x_axis, [statistics.median(i) for i in zip(*sample_acc)],linestyle='dashed', color='orange', label='sample median')




plt.ylabel("number of standard deviations")
plt.xlabel("sample size")
plt.legend(title=str(experiments_count) + ' experiments per sample size')
plt.gca().set_ylim(bottom=-1)
plt.grid()

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()

