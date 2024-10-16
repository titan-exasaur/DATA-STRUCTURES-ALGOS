import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def curve(t):
    return np.array([np.cos(t), np.sin(t), t])

def tangent(t):
    return np.array([-np.sin(t), np.cos(t), 1])

t = np.linspace(0, 4*np.pi, 100)
points = np.array([curve(ti) for ti in t])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(points[:, 0], points[:, 1], points[:, 2], label='Curve')

# Plot tangent vectors at several points
for ti in [0, np.pi/2, np.pi, 3*np.pi/2]:
    p = curve(ti)
    v = tangent(ti)
    ax.quiver(p[0], p[1], p[2], v[0], v[1], v[2], color='r', length=0.5, normalize=True)

ax.set_title('Space Curve with Tangent Vectors')
ax.legend()
plt.show()
