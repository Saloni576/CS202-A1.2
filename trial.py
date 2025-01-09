# some code from previous course assignmets of mine

import numpy as np
import matplotlib.pyplot as plt

a = 1.2
b = 0.6
c = 0.8
d = 0.3
x0 = 2.0
y0 = 1.0
t0 = 0.0
t_end = 20.0
h = 0.1  # Step size

t_values = np.arange(t0, t_end + h, h)
x_values = []
y_values = []

x = x0
y = y0

for t in t_values:
    x_values.append(x)
    y_values.append(y)
    
    dx_dt = a * x - b * x * y
    dy_dt = -c * y + d * x * y
    
    x += h * dx_dt
    y += h * dy_dt

# Print the first two and last two pairs of (x, y) values
print("First two pairs of (x, y) values:")
for i in range(3):
    print(f"({x_values[i]}, {y_values[i]})")

print("Last two pairs of (x, y) values:")
for i in range(len(t_values) - 3, len(t_values)):
    print(f"({x_values[i]}, {y_values[i]})")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t_values, x_values, label='Prey (x)')
plt.plot(t_values, y_values, label='Predators (y)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('Lotka-Volterra Predator-Prey Model Simulation (Euler\'s Method)')
plt.grid(True)
plt.show()