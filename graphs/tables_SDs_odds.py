
exec(open('stats.py').read())
#exec(open('graphs/tables_SDs_odds.py').read())

import numpy as np
import matplotlib.pyplot as plt
import time

#for some reason have to run this twice to get the formatting right, i don't understand...

fig, ax = plt.subplots()


font = {'family' : 'normal',
        'size'   : 9.5}

plt.rc('font', **font)


plt.rcParams["figure.figsize"] = [10, 1.4]
plt.xlabel("estimate 1:  -.4n²+.96n+.5        estimate 2:  n/10 + (7/4)√n -1/5", fontsize=11)
plt.setp(ax.spines.values(), visible=False)
ax.tick_params(left=False, labelleft=False,bottom=False, labelbottom=False )

def SD_odds_poly(n):
   return (n**2 + n + 2)/5

#cols = np.linspace(0, 8, 17)
#rows = ['SDs', '1 in 10ⁿ', '(x²+x+2)/5'] 
#data = [cols, [round(float(SD_odds(c)[1:]),1) for c in cols], [round(float(SD_odds_poly(c)),1) for c in cols]]
#title = 'SDs to rarity'

def odds_SDs_poly(n):
   return -0.04*n**2 + 0.96*n + .5

def odds_SDs_poly_sqrt(n):
   return (n/10 + np.sqrt(n)*7/4 - 1/5)

cols = np.linspace(.5, 14, 28)
rows = ['1/10ⁿ', 'SDs', 'est. 1', 'est. 2']
data = [cols, [round(odds_SDs(10**c), 1) for c in cols], [round(float(odds_SDs_poly(c)),1) for c in cols], [round(float(odds_SDs_poly_sqrt(c)),1) for c in cols]]

title = 'rarity to SDs'

t = ax.table(cellText=data,rowLabels=rows, loc='center',bbox = [0.0, 0, 1, 0.8])

t.auto_set_font_size(False)

plt.tight_layout() 

plt.rcParams["axes.titley"] =.82
plt.title(title)

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()
