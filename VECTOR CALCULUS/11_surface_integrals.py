import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbolic variables and surface
u, v = sp.symbols('u v')
x = u * sp.cos(v)
y = u * sp.sin(v)
z = u**2

# Calculate surface area
r_u = sp.Matrix([sp.diff(x, u), sp.diff(y, u), sp.diff(z, u)])
r_v = sp.Matrix([sp.diff(x, v), sp.diff(y, v), sp.diff(z, v)])
normal = r_u.cross(r_v)
surface_element = normal.norm()

surface_area = sp.integrate(sp.integrate(surface_element, (u, 0, 1)), (v, 0, 2*sp.pi))

print("Surface area of z = x^2 + y^2 for 0 ≤ √(x^2 + y^2) ≤ 1:")
print(surface_area)

# Visualize the surface
u_vals = np.linspace(0, 1, 50)
v_vals = np.linspace(0, 2*np.pi, 50)
U, V = np.meshgrid(u_vals, v_vals)
X = U * np.cos(V)
Y = U * np.sin(V)
Z = U**2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Surface z = x^2 + y^2')
plt.colorbar(surf)
plt.show()
