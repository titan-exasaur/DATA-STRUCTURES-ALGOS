import numpy as np
import matplotlib.pyplot as plt

# Define vector field
def P(x, y):
    return x**2 + y

def Q(x, y):
    return x - y**2

# Define curl
def curl(x, y):
    return -2*y - 2*x

# Create grid
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Calculate vector field
U = P(X, Y)
V = Q(X, Y)

# Plot vector field
plt.figure(figsize=(10, 8))
plt.quiver(X, Y, U, V)

# Plot unit circle
theta = np.linspace(0, 2*np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
plt.plot(x_circle, y_circle, 'r-', linewidth=2)

plt.title("Vector Field and Region for Green's Theorem")
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.show()

# Note: Actual integration would require symbolic computation
print("Green's Theorem states that the line integral")
print("around the unit circle equals the double integral")
print("of the curl over the enclosed region.")
