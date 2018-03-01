import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi,np.pi,0.01)
z = 0
for n in range(100):
    z = z + np.cos(2*n*x) / (4*n ** 2 - 1)


y = 1/np.pi + np.sin(x) / 2 - 2/ np.pi * z

plt.plot(x,y)

plt.show()
