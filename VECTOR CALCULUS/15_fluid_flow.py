import numpy as np
import matplotlib.pyplot as plt

# Pipe parameters
L = 10  # length
R1, R2 = 2, 1  # radii at ends

# Generate pipe shape
x = np.linspace(0, L, 100)
r = R1 + (R2 - R1) * x / L

# Calculate velocity (assuming constant flow rate)
Q = 10  # flow rate
v = Q / (np.pi * r**2)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(x, r, 'b', label='Pipe radius')
plt.plot(x, -r, 'b')
plt.plot(x, v, 'r', label='Fluid velocity')
plt.title('Fluid Flow in a Converging Pipe')
plt.xlabel('Distance along pipe')
plt.ylabel('Radius / Velocity')
plt.legend()
plt.grid(True)
plt.show()

print("The continuity equation states: A1v1 = A2v2")
print("where A is cross-sectional area and v is velocity.")
print("This demonstrates conservation of mass in fluid flow.")
