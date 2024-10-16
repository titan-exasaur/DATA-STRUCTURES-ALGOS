import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbolic variables and function
x, y = sp.symbols('x y')
f = x**2 - y**2

# Calculate gradient
grad_f = sp.Matrix([sp.diff(f, x), sp.diff(f, y)])

print("Function f(x, y):", f)
print("Gradient ∇f:", grad_f)

# Calculate directional derivative
u = sp.Matrix([1, 1])  # Direction vector
dir_deriv = grad_f.dot(u.normalized())

print("Directional derivative in direction [1, 1]:", dir_deriv)

# Visualize gradient vector field
x_vals = y_vals = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x_vals, y_vals)
U = 2 * X
V = -2 * Y

plt.figure(figsize=(10, 8))
plt.quiver(X, Y, U, V, scale=50)
plt.title('Gradient Vector Field of f(x, y) = x² - y²')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
