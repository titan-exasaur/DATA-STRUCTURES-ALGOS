import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import combinations, product


# Define vector field
def F(x, y, z):
    return np.array([x, y, z])

# Define divergence
def div_F(x, y, z):
    return 3  # div F = ∂F_x/∂x + ∂F_y/∂y + ∂F_z/∂z = 1 + 1 + 1 = 3

# Create a cube
r = [-1, 1]
x, y, z = np.meshgrid(r, r, r)

# Calculate vector field at cube vertices
u, v, w = F(x, y, z)

# Plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot cube edges
for s, e in zip(combinations(np.array(list(product(r, r, r))), 2), product([0, 1, 2], repeat=2)):
    if np.sum(np.abs(s[0] - e[0])) == r[1] - r[0]:
        ax.plot3D(*zip(s[0], e[0]), color="b")

# Plot vector field
ax.quiver(x, y, z, u, v, w, length=0.2, normalize=True)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Cube and Vector Field for Divergence Theorem")

plt.show()

print("The Divergence Theorem states that the surface integral")
print("of F • n over the cube's surface equals the volume integral")
print("of div F throughout the cube.")
print(f"Here, div F = {div_F(0, 0, 0)} everywhere.")
