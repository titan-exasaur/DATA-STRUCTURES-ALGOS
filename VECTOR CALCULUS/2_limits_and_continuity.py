import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.array([t**2, np.sin(t)])

t = np.linspace(-5, 5, 1000)
x, y = f(t)

plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title('Continuous Vector Function')
plt.xlabel('x = t^2')
plt.ylabel('y = sin(t)')
plt.grid(True)
plt.show()

# Check continuity at t = 0
t0 = 0
limit = f(t0)
print(f"Limit at t = {t0}: {limit}")
print(f"Function value at t = {t0}: {f(t0)}")
print("The function is continuous at t = 0")
