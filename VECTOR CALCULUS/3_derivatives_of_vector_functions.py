import sympy as sp

# Define symbolic variable and vector function
t = sp.Symbol('t')
r = sp.Matrix([sp.cos(t), sp.sin(t), t**2])

# Calculate derivative
r_prime = r.diff(t)

print("Vector function r(t):")
print(r)
print("\nDerivative r'(t):")
print(r_prime)

# Evaluate at t = π/4
t_val = sp.pi/4
r_val = r.subs(t, t_val)
r_prime_val = r_prime.subs(t, t_val)

print(f"\nAt t = π/4:")
print(f"r(π/4) = {r_val.evalf()}")
print(f"r'(π/4) = {r_prime_val.evalf()}")
