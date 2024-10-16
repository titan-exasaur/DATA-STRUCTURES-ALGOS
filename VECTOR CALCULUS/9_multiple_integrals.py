import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbolic variables and function
x, y = sp.symbols('x y')
f = sp.sin(x) * sp.cos(y)

# Calculate double integral
integral = sp.integrate(sp.integrate(f, (y, 0, sp.pi/2)), (x, 0, sp.pi/2))

print("Double integral of sin(x)cos(y) over [0, π/2] × [0, π/2]:")
print(integral)

# Visualize the function
x_vals = y_vals = np.linspace(0, np.pi/2, 50)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.sin(X) * np.cos(Y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('f(x, y) = sin(x)cos(y)')
plt.colorbar(surf)
plt.show()
