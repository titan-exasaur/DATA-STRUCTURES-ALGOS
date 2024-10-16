import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vector field
def F(x, y, z):
    return np.array([y, z, x])

# Define surface (part of a sphere)
theta = np.linspace(0, np.pi/2, 30)
phi = np.linspace(0, np.pi, 30)
THETA, PHI = np.meshgrid(theta, phi)

R = 2  # radius
X = R * np.sin(PHI) * np.cos(THETA)
Y = R * np.sin(PHI) * np.sin(THETA)
Z = R * np.cos(PHI)

# Plot surface and vector field
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.3)

# Sample points for vector field
u = np.linspace(0, 2, 5)
v = np.linspace(0, 2, 5)
U, V = np.meshgrid(u, v)

x = U
y = V
z = np.sqrt(R**2 - x**2 - y**2)

Fx, Fy, Fz = F(x, y, z)

ax.quiver(x, y, z, Fx, Fy, Fz, length=0.5, normalize=True)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Surface and Vector Field for Stokes' Theorem")

plt.show()

print("Stokes' Theorem relates the surface integral of curl F")
print("over this portion of the sphere to the line integral of F")
print("around its boundary curve.")
