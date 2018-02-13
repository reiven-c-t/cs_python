import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,50,0.1)
z = 0
for n in range(100):
    z = z + (np.cos(2*n-1) * x) / (2 * n -1) ** 2


y = 2/np.pi - 4/ np.pi * z

plt.plot(x,y)

plt.show()
