import numpy as np
import matplotlib.pyplot as plt

b = np.loadtxt('scan.dat',skiprows=2)
#a = np.loadtxt('big.dat',skiprows=59)
#print(a)
#ind = np.argsort(a[:,-1])
#b = a[ind]
#b[:,1] -= min(b[:,1])
#b[:,1] *= 627.509
#print(b)

plt.figure()
plt.plot(b[:,0],b[:,1],'ko')
plt.show()

