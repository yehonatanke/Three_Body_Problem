# gravitational_system.py

import numpy as np


def derivs(state, t):
    """
    Compute the derivatives of position and velocity.

    Args:
    state (array_like): State vector containing positions and velocities of all bodies.
    t (float): Time.

    Returns:
    list: List of derivatives.
    """
    # Define constants
    G = 6.67430e-11  # Gravitational constant

    # Unpack state vector
    x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3 = state

    # Masses of the Sun, Earth, and Jupiter (in kg)
    m1 = 1.989e30  # Mass of the Sun
    m2 = 5.972e24  # Mass of the Earth
    m3 = 1.898e27  # Mass of Jupiter

    # Derivatives
    dxdt1 = vx1
    dydt1 = vy1
    dvxdt1 = G * ((m2 * (x2 - x1) / ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1.5) +
                  (m3 * (x3 - x1) / ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 1.5))
    dvydt1 = G * ((m2 * (y2 - y1) / ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1.5) +
                  (m3 * (y3 - y1) / ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 1.5))

    dxdt2 = vx2
    dydt2 = vy2
    dvxdt2 = G * ((m1 * (x1 - x2) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1.5) +
                  (m3 * (x3 - x2) / ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 1.5))
    dvydt2 = G * ((m1 * (y1 - y2) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1.5) +
                  (m3 * (y3 - y2) / ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 1.5))

    dxdt3 = vx3
    dydt3 = vy3
    dvxdt3 = G * ((m1 * (x1 - x3) / ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 1.5) +
                  (m2 * (x2 - x3) / ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 1.5))
    dvydt3 = G * ((m1 * (y1 - y3) / ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 1.5) +
                  (m2 * (y2 - y3) / ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 1.5))

    return [dxdt1, dydt1, dvxdt1, dvydt1,
            dxdt2, dydt2, dvxdt2, dvydt2,
            dxdt3, dydt3, dvxdt3, dvydt3]
