import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,10,1)
print(x)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
factorial = np.vectorize(factorial)
def power(n):
    return n ** n
power = np.vectorize(power)

fig, ax = plt.subplots()
ax.plot(x,np.exp(x),'ko')
ax.plot(x,factorial(x),'bo')
ax.plot(x,power(x),'go')
plt.yscale('log')
plt.show()
