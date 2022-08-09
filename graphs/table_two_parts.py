import numpy as np
import matplotlib.pyplot as plt
import time

#exec(open('graphs/table_two_parts.py').read())
exec(open('stats.py').read())
#for some reason have to run this twice to get the formatting right, i don't understand...

fig, ax = plt.subplots()

plt.rcParams["figure.figsize"] = [10, 3]
plt.axis('off')

cols = [2,3,4,5,6,10,30,100,1000,10000, 100000,1000000, ]
rows = cols

def numerical_sum_estimate(r,c):
   return gaussian_max_numerical(r, 1/np.sqrt(2), 0) + gaussian_max_numerical(c, 1/np.sqrt(2), 0)

#def median_sum_estimate(r,c):
#   return gaussian_max_median(r, 1/np.sqrt(2), 0) + gaussian_max_median(c, 1/np.sqrt(2), 0)

# table of the sum SDs
#data = [[round(numerical_sum_estimate(r,c),2) for r in rows] for c in cols]
#title = "1 in [row] + 1 in [col] in standard deviations"

# table of the error of the approximation
def apx(r,c):
   lr, lc = np.log10(r), np.log10(c)
   return (lr + lc)/2 +1

def error(r,c):
   exact = numerical_sum_estimate(r,c)
# table of the error of the median approximation from numerical integration
#   approx = float(SD_odds(median_sum_estimate(r,c))[1:])
   approx = apx(r,c)
   return (exact-approx)

data = [[round(error(r,c),2) for r in rows] for c in cols] 
title = "error: [1 in R + 1 in C] - [1 + (log₁₀(R) + log₁₀(C))/2], in standard deviations"


colors = [[ [['w', (.8,.8,1),],[(1,.8,.8),(.8,.6,.8)]][i%2==0][j%2==0]  for j,_ in enumerate(rows) ] for i,_ in enumerate(cols) ] 

t = ax.table(cellText=data,colLabels=["{:,}".format(c) for c in cols],rowLabels=["{:,}".format(r) for r in rows], loc='center',cellColours=colors)

t.auto_set_font_size(False)

plt.tight_layout() 



plt.rcParams["axes.titley"] =.97
plt.title(title)

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()
