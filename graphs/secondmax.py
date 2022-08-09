from matplotlib import pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
import time

#exec(open('graphs/secondmax.py').read())
exec(open('stats.py').read())

plt.rcParams["figure.figsize"] = [10, 8]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()

plt.xscale('log')
x_max = 5
x_axis = np.ndarray.astype(10**np.linspace(.4, x_max+.4, 10*x_max) , 'int')
x_axis_left_offset = 10**np.linspace(.37, x_max+.37, 10*x_max)
x_axis_right_offset = 10**np.linspace(.43, x_max+.43, 10*x_max)

ax.plot(x_axis, [gaussian_max_numerical(x, 1, 0) for x in x_axis], color='purple',linestyle='solid', label='maximum, numerical')

experiments_count = 80
sample_acc = []
for _ in range(experiments_count):
   samples = [gaussian_max_sample(sample_count, 1, 0) for sample_count in x_axis] 
   sample_acc.append(samples)
   ax.scatter(x_axis_right_offset, samples, color='green', s=73, alpha=.08, edgecolor='none')

ax.plot(x_axis, [sum(i)/experiments_count for i in zip(*sample_acc)],linestyle='dotted', color='black', label='sample mean')
ax.plot(x_axis, [statistics.median(i) for i in zip(*sample_acc)],linestyle='dashed', color='orange', label='sample median')

ax.plot(x_axis, [gaussian_secondmax_numerical(x, 1, 0) for x in x_axis], color='black',linestyle='solid', label='2nd maximum, numerical')

second_sample_acc = []
for _ in range(experiments_count):
   samples = [gaussian_secondmax_sample(sample_count, 1, 0) for sample_count in x_axis] 
   second_sample_acc.append(samples)
   ax.scatter(x_axis_left_offset, samples, color='red', s=73, alpha=.08, edgecolor='none')

ax.plot(x_axis, [sum(i)/experiments_count for i in zip(*second_sample_acc)],linestyle='dotted', color='black',) 
ax.plot(x_axis, [statistics.median(i) for i in zip(*second_sample_acc)],linestyle='dashed', color='orange', )



plt.ylabel("number of standard deviations")
plt.xlabel("sample size   [note: samples x-offset for visibility]")
plt.legend(title=str(experiments_count) + ' experiments per sample size')
plt.gca().set_ylim(bottom=-1)
plt.grid()

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()

