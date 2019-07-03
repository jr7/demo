import numpy as np
import matplotlib.pyplot as plt

from functions import sin, cos

x  = np.linspace(0, 10, 10000)
plt.plot(x, sin(x))
plt.plot(x, cos(x))

plt.show()
