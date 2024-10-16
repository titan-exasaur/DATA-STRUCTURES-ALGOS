import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbolic variables and vector field
t, x, y = sp.symbols('t x y')
F = sp.Matrix([y, x])

# Define parametric curve
r = sp.Matrix([sp.cos(t), sp.sin(t)])

# Calculate line integral
integrand = F.dot(r.diff(t))
line_integral = sp.integrate(integrand, (t, 0, 2*sp.pi))

print("Line integral of F = [y, x] along the unit circle:")
print(line_integral)

# Visualize vector field and curve
x_vals = y_vals = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x_vals, y_vals)
U = Y
V = X

plt.figure(figsize=(10, 8))
plt.quiver(X, Y, U, V)
theta = np.linspace(0, 2*np.pi, 100)
x_curve = np.cos(theta)
y_curve = np.sin(theta)
plt.plot(x_curve, y_curve, 'r-', linewidth=2)
plt.title('Vector Field F = [y, x] and Unit Circle')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.show()
