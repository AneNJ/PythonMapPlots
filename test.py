import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,10,0.1)

for n in np.arange(1,4,1):
    y = np.sin(n*x)
    z = np.cos(n*x)
    plt.plot(x,y,"r")
    plt.plot(x,z,"b")

plt.show()
