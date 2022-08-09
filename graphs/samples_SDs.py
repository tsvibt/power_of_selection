from matplotlib import pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
import time

#exec(open('graphs/samples_SDs.py').read())
exec(open('stats.py').read())

plt.rcParams["figure.figsize"] = [10, 8]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()

plt.xscale('log')
x_max = 7
x_axis = np.ndarray.astype(10**np.linspace(.4, x_max+.4, 10*x_max) , 'int')

ax.plot(x_axis, [gaussian_inv_cdf(1, 0, (x-1)/x) for x in x_axis], color='purple',linestyle='solid', label='Φ⁻¹((x-1)/x)')

plt.ylabel("number of standard deviations")
plt.xlabel("rarity, 1 in x")
plt.legend()
plt.gca().set_ylim(bottom=-1)
plt.grid()

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()

