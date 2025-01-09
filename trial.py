"""
This script simulates the Lotka-Volterra predator-prey model using Euler's method.
It calculates and plots the population dynamics of prey and predators over time.
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants for the Lotka-Volterra equations
SIMULATION_PARAMS = {
    "a": 1.2,
    "b": 0.6,
    "c": 0.8,
    "d": 0.3,
    "x0": 2.0,
    "y0": 1.0,
    "t0": 0.0,
    "t_end": 20.0,
    "h": 0.1
}

def lotka_volterra_simulation(params):
    """
    Simulates the Lotka-Volterra predator-prey model using Euler's method.

    Args:
        params (dict): A dictionary containing simulation parameters:
            - a, b, c, d: Lotka-Volterra constants.
            - x0, y0: Initial populations of prey and predators.
            - t0, t_end: Start and end times for simulation.
            - h: Time step size.

    Returns:
        tuple: Arrays for time, prey population, and predator population.
    """
    t_values = np.arange(params["t0"], params["t_end"] + params["h"], params["h"])
    x_values, y_values = [], []
    x, y = params["x0"], params["y0"]

    for _ in t_values:
        x_values.append(x)
        y_values.append(y)
        dx_dt = params["a"] * x - params["b"] * x * y
        dy_dt = -params["c"] * y + params["d"] * x * y
        x += params["h"] * dx_dt
        y += params["h"] * dy_dt

    return t_values, x_values, y_values

def main():
    """
    Main function to simulate and plot the Lotka-Volterra model.
    """
    t_values, x_values, y_values = lotka_volterra_simulation(SIMULATION_PARAMS)

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
