from matplotlib import pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
import time

#exec(open('graphs/top_two_sum_linear.py').read())
exec(open('stats.py').read())

plt.rcParams["figure.figsize"] = [10, 8]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()

x_max = 30 
x_axis = np.ndarray.astype(np.linspace(2, x_max, x_max-1) , 'int')

ax.plot(x_axis, [gaussian_firstsecondmax_numerical(x,1,0)/np.sqrt(2) for x in x_axis], color='purple',linestyle='solid', label='new numerical')

experiments_count = 150
sample_acc = []
for _ in range(experiments_count):
   samples = [(gaussian_firstsecondmax_sample(sample_count, 1, 0))/np.sqrt(2) for sample_count in x_axis] 
   sample_acc.append(samples)
   ax.scatter(x_axis, samples, color='green', s=89, alpha=.08, edgecolor='none')

ax.plot(x_axis, [sum(i)/experiments_count for i in zip(*sample_acc)],linestyle='dotted', color='black', label='sample mean')
ax.plot(x_axis, [statistics.median(i) for i in zip(*sample_acc)],linestyle='dashed', color='orange', label='sample median')

loc = plticker.MultipleLocator(base=1.0) 
ax.xaxis.set_major_locator(loc)

plt.ylabel("number of standard deviations (of the sum of two samples)")
plt.xlabel("sample size")
plt.legend(title=str(experiments_count) + ' experiments per sample size')
plt.gca().set_ylim(bottom=-1)
plt.grid()

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()

