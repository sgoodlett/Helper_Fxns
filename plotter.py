import matplotlib.pyplot as plt
import numpy as np


oo = [1.809,1.802,1.802,1.802,1.929,1.901,1.898,1.897,2.024,2.000,1.990,1.988]
a = [91.08,91.18,91.15,91.16,83.35,83.03,83.19,83.05,84.09,83.66,83.75,83.76]


fig, ax1 = plt.subplots()
ax1.set_xlabel('Iteration')
ax1.set_ylim(1.8,2.055)
ax1.set_ylabel('Distance in Angstroms')
ax1.plot(oo, 'b-',label='O--O Distance')
plt.legend(loc=(0.7,0.55))
ax2 = ax1.twinx()
ax2.set_ylim(80,93)
ax2.set_ylabel('Angle')
ax2.plot(a,'r-',label='Angle')
plt.legend(loc=(0.7,0.45))
plt.savefig('bl_a.png')
