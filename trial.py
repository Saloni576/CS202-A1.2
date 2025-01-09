"""
This script simulates the Lotka-Volterra predator-prey model using Euler's method.
It calculates and plots the population dynamics of prey and predators over time.
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants for the Lotka-Volterra equations
A = 1.2  
B = 0.6  
C = 0.8  
D = 0.3  
X0 = 2.0  
Y0 = 1.0  
T0 = 0.0  
T_END = 20.0  
H = 0.1  

def lotka_volterra_simulation(a, b, c, d, x0, y0, t0, t_end, h):
    """
    Simulates the Lotka-Volterra predator-prey model using Euler's method.
    """
    t_values = np.arange(t0, t_end + h, h)
    x_values = []
    y_values = []
    x, y = x0, y0

    for t in t_values:
        x_values.append(x)
        y_values.append(y)
        dx_dt = a * x - b * x * y
        dy_dt = -c * y + d * x * y
        x += h * dx_dt
        y += h * dy_dt

    return t_values, x_values, y_values

def main():
    """
    Main function to simulate and plot the Lotka-Volterra model.
    """
    t_values, x_values, y_values = lotka_volterra_simulation(A, B, C, D, X0, Y0, T0, T_END, H)

    # Print results
    print("First two pairs of (x, y) values:")
    for i in range(3):
        print(f"({x_values[i]}, {y_values[i]})")

    print("Last two pairs of (x, y) values:")
    for i in range(len(t_values) - 3, len(t_values)):
        print(f"({x_values[i]}, {y_values[i]})")

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, x_values, label='Prey (x)')
    plt.plot(t_values, y_values, label='Predators (y)')
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.legend()
    plt.title('Lotka-Volterra Predator-Prey Model Simulation (Euler\'s Method)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
