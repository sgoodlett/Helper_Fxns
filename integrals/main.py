from scipy.integrate import nquad
import numpy as np
import matplotlib.pyplot as plt
from sys import argv


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

if argv[1] == 'g':
    def fxn(x,y,z,zeta,nx,ny,nz):
        nx *= nx
        ny *= ny
        nz *= nz
        r = np.sqrt((x**2)+(y**2)+(z**2))
        a = (x**nx)*(y**ny)*(z**nz)*np.exp(-2*zeta*r)
        return 2 * a
    m = 15
    x = np.asarray(range(m))
    y = np.zeros(m)
    for i in range(m):
        intval, err = nquad(lambda x, y, z : fxn(x,y,z,i,1,0,0),[[0,1000],[0,1000],[0,1000]])
        print(f'{i}:   {err}\n\n')
        N = intval ** -0.5
        y[i] = N
    np.savetxt('x.txt',x)
    np.savetxt('y.txt',y)
elif argv[1] == 'p':
    x = np.loadtxt('x.txt')
    y = np.loadtxt('y.txt')
    plt.figure()
    plt.plot(x,y,'k-')
    #plt.plot(x,[i**2 for i in range(len(x))],'b-')
    #plt.plot(x,[i**3 for i in range(len(x))],'b-')
    plt.plot(x,[np.exp(i) for i in range(len(x))],'b-')
    plt.plot(x,[fact(i) for i in range(len(x))],'r-')

    plt.yscale('log')
    plt.show()


