import sympy as sp

# Define symbolic variable and vector function
t = sp.Symbol('t')
r = sp.Matrix([sp.cos(t), sp.sin(t), t])

# Calculate derivatives
r_prime = r.diff(t)
r_double_prime = r_prime.diff(t)
r_triple_prime = r_double_prime.diff(t)

# Calculate curvature
curvature = (r_prime.cross(r_double_prime).norm() / r_prime.norm()**3)

# Calculate torsion
torsion = (r_prime.dot(r_double_prime.cross(r_triple_prime)) / 
           r_prime.cross(r_double_prime).norm()**2)

print("Curvature:")
print(curvature.simplify())
print("\nTorsion:")
print(torsion.simplify())

# Evaluate at t = π/4
t_val = sp.pi/4
curvature_val = curvature.subs(t, t_val)
torsion_val = torsion.subs(t, t_val)

print(f"\nAt t = π/4:")
print(f"Curvature = {curvature_val.evalf()}")
print(f"Torsion = {torsion_val.evalf()}")
