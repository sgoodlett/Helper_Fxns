import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt('data.dat')
a[:,1] *= 627.509
a[:,1] -= min(a[:,1])
plt.figure()
plt.plot(a[:,0], a[:,1], 'ko')
plt.show()

