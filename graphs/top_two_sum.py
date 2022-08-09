from matplotlib import pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
import time

#exec(open('graphs/top_two_sum.py').read())
exec(open('stats.py').read())

plt.rcParams["figure.figsize"] = [10, 8]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()

plt.xscale('log')
x_max = 5
x_axis = np.ndarray.astype(10**np.linspace(.4, x_max+.4, 10*x_max) , 'int')

ax.plot(x_axis, [(gaussian_max_numerical(x, 1, 0) + gaussian_secondmax_numerical(x, 1, 0))/np.sqrt(2) for x in x_axis], color='purple',linestyle='solid', label='(E(max) + E(2nd))/√2, numerical')

experiments_count = 100
sample_acc = []
for _ in range(experiments_count):
   samples = [gaussian_firstsecondmax_sample(sample_count, 1, 0)/np.sqrt(2) for sample_count in x_axis] 
   sample_acc.append(samples)
   ax.scatter(x_axis, samples, color='green', s=73, alpha=.08, edgecolor='none')

ax.plot(x_axis, [sum(i)/experiments_count for i in zip(*sample_acc)],linestyle='dotted', color='black', label='sample mean')
ax.plot(x_axis, [statistics.median(i) for i in zip(*sample_acc)],linestyle='dashed', color='orange', label='sample median')



plt.ylabel("number of standard deviations (of the sum of two samples)")
plt.xlabel("sample size")
plt.legend(title=str(experiments_count) + ' experiments per sample size')
plt.gca().set_ylim(bottom=-1)
plt.grid()

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()

