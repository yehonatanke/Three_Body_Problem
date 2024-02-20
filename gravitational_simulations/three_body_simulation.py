# three_body_simulation.py

import numpy as np
from scipy.integrate import odeint
from gravitational_system import derivs
from plot_animation import plot_animation


def main():
    # Initial conditions (position and velocity)
    state0 = [-1.4710e11, 0, 0, -3.0287e4,  # Sun: x, y, vx, vy
              0, 1.4709e11, 3.0287e4, 0,  # Earth: x, y, vx, vy
              0, -7.405e11, -1.228e4, 0]  # Jupiter: x, y, vx, vy

    # Time array (simulate for 1 year)
    t = np.linspace(0, 365 * 24 * 3600, 1000)

    # Solve the differential equations
    state = odeint(derivs, state0, t)

    # Plot trajectories and create animation
    plot_animation(state)


if __name__ == "__main__":
    main()
