import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbolic variables and function
x, y = sp.symbols('x y')
f = x**2 + y**2

# Calculate partial derivatives
fx = sp.diff(f, x)
fy = sp.diff(f, y)

print("Function f(x, y):", f)
print("∂f/∂x =", fx)
print("∂f/∂y =", fy)

# Create a 3D plot of the function
x_vals = y_vals = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = X**2 + Y**2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('f(x, y) = x² + y²')
plt.colorbar(surf)
plt.show()
