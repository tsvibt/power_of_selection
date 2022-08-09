import numpy as np
import matplotlib.pyplot as plt
import time

#exec(open('graphs/table_k_parts.py').read())
exec(open('stats.py').read())
#for some reason have to run this twice to get the formatting right, i don't understand...

fig, ax = plt.subplots()

plt.rcParams["figure.figsize"] = [9, 3.8]
#plt.axis('off')


plt.xlabel("samples selected from")
plt.ylabel("number of subdivisions")
plt.setp(ax.spines.values(), visible=False)
ax.tick_params(left=False, labelleft=False,bottom=False, labelbottom=False )
ax.yaxis.set_label_coords(-.08, .5)


cols = [2,3,4,5,6,10,30,100,1000,10000, 100000, ]
rows = [2,3,4,5,6,10,23,46,92,138,184,460,1000,10000, 100000, ]

# graph of the sum rarity

data = [[round(np.sqrt(division_count)*(gaussian_max_numerical(sample_size,1,0)),2) for sample_size in cols] for division_count in rows] 
title = "cells show SDs of maximum"


colors = [[ [['w', (.8,.8,1),],[(1,.8,.8),(.8,.6,.8)]][i%2==0][j%2==0]  for i,_ in enumerate(cols) ] for j,_ in enumerate(rows) ] 

ax.table(cellText=data,colLabels=cols,rowLabels=rows, loc='center',cellColours=colors)

plt.tight_layout() 



plt.rcParams["axes.titley"] =.95
plt.title(title)

#plt.savefig('./output/graph' + str(round(time.time())) + '.png')

plt.show()


