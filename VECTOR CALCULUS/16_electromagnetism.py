import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a point charge
q = 1  # charge
k = 1  # Coulomb's constant (simplified)

# Define electric field
def E(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    return k * q * np.array([x, y, z]) / (r**3)

# Create grid
x, y, z = np.meshgrid(np.linspace(-2, 2, 5),
                      np.linspace(-2, 2, 5),
                      np.linspace(-2, 2, 5))

# Calculate electric field
Ex, Ey, Ez = E(x, y, z)

# Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot electric field vectors
ax.quiver(x, y, z, Ex, Ey, Ez, length=0.5, normalize=True)

# Plot charge
ax.scatter([0], [0], [0], color='r', s=100, label='Point charge')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Electric Field of a Point Charge")
ax.legend()

plt.show()

print("Gauss's Law: ∮ E • dA = q / ε₀")
print("This relates the electric field flux through a closed surface")
print("to the enclosed charge, demonstrating the Divergence Theorem.")
