import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def helix(t):
    return np.array([np.cos(t), np.sin(t), t])

t = np.linspace(0, 10*np.pi, 1000)
x, y, z = helix(t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_title('Helix: A Space Curve')
plt.show()
