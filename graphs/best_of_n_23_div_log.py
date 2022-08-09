from matplotlib import pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
import time

#exec(open('graphs/best_of_n_23_div_log.py').read())
exec(open('stats.py').read())

plt.rcParams["figure.figsize"] = [10, 8]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()

haploid_chromosome_count = 23

chromosome_lengths = {1: 247249719, 2: 242951149, 3: 199501827, 4: 191273063, 5: 180857866, 6: 170899992, 7: 158821424, 8: 146274826, 9: 140273252, 10: 135374737, 11: 134452384, 12: 132349534, 13: 114142980, 14: 106368585, 15: 100338915, 16: 88827254, 17: 78774742, 18: 76117153, 19: 63811651, 20: 62435964, 21: 46944323, 22: 49691432, 'Y': 57772954, 'X': 154913754}
full_genome_length = sum([2*v for k,v in chromosome_lengths.items() if k!='Y'])

plt.xscale('log')
x_max = 5
seed_genome_counts = np.ndarray.astype(10**np.linspace(.4, x_max+.4, 10*x_max) , 'int')
samples_count = 70

def genomes_top_sum_numerical(seed_genome_count):
   return sum([ gaussian_max_numerical(2*seed_genome_count, division_variance(full_genome_length / chromosome_length), 0) for chromosome_number, chromosome_length in chromosome_lengths.items() if chromosome_number not in ['X','Y'] ])

ax.plot(seed_genome_counts, [genomes_top_sum_numerical(seed_genome_count) for seed_genome_count in seed_genome_counts],linestyle='solid', color='red', label='numerical, sum of expected values by chromosome length')


# sampling
sample_acc = []
for _ in range(samples_count):
   samples = [sum([gaussian_max_sample(2*seed_genome_count, division_variance(full_genome_length / chromosome_length), 0) for chromosome_number, chromosome_length in chromosome_lengths.items() if chromosome_number not in ['X', 'Y']]) for seed_genome_count in seed_genome_counts]
   sample_acc.append(samples)
   ax.scatter(seed_genome_counts, samples, color='green', s=83, alpha=.08, edgecolor='none')

ax.plot(seed_genome_counts, [sum(i)/samples_count for i in zip(*sample_acc)],linestyle='dotted', color='black', label='sample mean')
ax.plot(seed_genome_counts, [statistics.median(i) for i in zip(*sample_acc)],linestyle='dashed', color='orange', label='sample median')

loc = plticker.MultipleLocator(base=1.0) 
ax.yaxis.set_major_locator(loc)

plt.ylabel("number of SDs of full genome, where unselected chromosomes are assumed mean (i.e. 0)")
plt.xlabel("number of random full genomes selected from")

plt.legend(title='scores of full genome with one top haploid genome selected\n23rd chromosome not selected\nestimate methods:')
plt.gca().set_ylim(bottom=-.1)
plt.grid()

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()

