from matplotlib import pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
import time

#exec(open('graphs/max_median.py').read())
exec(open('stats.py').read())

plt.rcParams["figure.figsize"] = [10, 8]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()

plt.xscale('log')
x_max = 7
x_axis = np.ndarray.astype(10**np.linspace(.4, x_max+.4, 10*x_max) , 'int')

ax.plot(x_axis, [gaussian_max_median(x, 1, 0) for x in x_axis], color='purple',linestyle='solid', label='Φ⁻¹((1/2)^(1/x))')

ax.plot(x_axis, [gaussian_max_numerical(x, 1, 0) for x in x_axis], color='red',linestyle='solid', label='numerical')


plt.ylabel("number of standard deviations")
plt.xlabel("sample size")
plt.legend()
plt.gca().set_ylim(bottom=-1)
plt.grid()

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()

