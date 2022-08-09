from matplotlib import pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
import time

#exec(open('graphs/max_cdfs_pdfs.py').read())
exec(open('stats.py').read())

plt.rcParams["figure.figsize"] = [10, 8]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()

x_axis = np.linspace(-1, 8, 200)

include_secondmax = True 
include_CDFs = False

for sample_size, color in zip([2, 10,  100, 10000, 100000000], ['orange', 'red', 'purple', 'green', 'blue', ]):
   plt.plot(x_axis, [gaussian_max_pdf(sample_size, 1, 0, z) for z in x_axis], color=color,linestyle='solid',  label="{:,}".format(sample_size) + ' samples')
   if include_CDFs:
      plt.plot(x_axis, [gaussian_max_cdf(sample_size, 1, 0, z) for z in x_axis], color=color,linestyle='dotted',) 
   if include_secondmax: 
      plt.plot(x_axis, [gaussian_secondmax_pdf(sample_size, 1, 0, z) for z in x_axis], color=color,linestyle='dashed',  )
      if include_CDFs:
         plt.plot(x_axis, [gaussian_secondmax_cdf(sample_size, 1, 0, z) for z in x_axis], color=color,linestyle='dashdot', )


plt.plot([], [], color='black',linestyle='solid', label='PDF of max of gaussians')
if include_CDFs:
   plt.plot([], [], color='black',linestyle='dotted', label='CDF of max of gaussians')
if include_secondmax: 
   plt.plot([], [], color='black',linestyle='dashed', label='PDF of 2nd max of gaussians')
   if include_CDFs:
      plt.plot([], [], color='black',linestyle='dashdot', label='CDF of 2nd max of gaussians')


loc = plticker.MultipleLocator(base=1.0) 
ax.xaxis.set_major_locator(loc)
loc = plticker.MultipleLocator(base=1.0) 
ax.yaxis.set_major_locator(loc)

plt.ylabel("probability (total or density)")
plt.xlabel("standard deviations")
plt.legend()
plt.gca().set_ylim(bottom=-.1)
plt.grid()

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()

