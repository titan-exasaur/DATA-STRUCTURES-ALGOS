import numpy as np
import sympy as sp

# Define symbolic variable and vector function
t = sp.Symbol('t')
r = sp.Matrix([sp.cos(t), sp.sin(t), t])

# Calculate derivative
r_prime = r.diff(t)

# Arc length function
arc_length = sp.integrate(sp.sqrt(sum(r_prime[i]**2 for i in range(3))), (t, 0, t))

print("Arc length function:")
print(arc_length)

# Calculate arc length for a specific interval
t1, t2 = 0, np.pi
length = arc_length.subs(t, t2) - arc_length.subs(t, t1)

print(f"\nArc length from t = {t1} to t = {t2}:")
print(length.evalf())