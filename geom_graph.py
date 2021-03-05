import matplotlib.pyplot as plt
import numpy as np

force_geom =   [
            [-0.000439,  2.050317],
	    [-0.000678,  2.049626],
	    [ 0.000517,  2.050151],
	    [-0.000069,  2.050040],
	    [-0.000395,  2.049111],
	    [ 0.001774,  2.049985],
	    [ 0.001550,  2.050214],
	    [-0.002282,  2.049623],
	    [-0.000956,  2.049528],
	    [ 0.000809,  2.050237],
	    [ 0.001313,  2.050013],
	    [ 0.000489,  2.050170],
	    [ 0.001535,  2.050072],
	    [-0.000249,  2.049892],
	    [ 0.001765,  2.049560],
	    [ 0.000308,  2.049485]]
force_geom = np.asarray(force_geom)



fig, ax1 = plt.subplots()
ax1.set_xlabel('Iteration')
#ax1.set_ylim(2.045,2.054)
#ax1.set_ylabel('Distance in Angstroms')
ax1.plot(force_geom[:,1], force_geom[:,0], 'bo',label='O--O Distance')
#plt.legend(loc=(0.6,0.25))
#ax2 = ax1.twinx()
#ax2.set_ylim(-0.002,0.015)
#ax2.set_ylabel('Max Force')
#ax2.plot(force_geom[:,0],'r-',label='O--O Max Force')
#plt.legend(loc=(0.6,0.45))
plt.savefig('fig.png')
