# Three Body Simulation

This project simulates the motion of the Sun, Earth, and Jupiter in the solar system using numerical integration techniques. The simulation is based on solving the differential equations of motion for the three bodies interacting gravitationally.

## Mathematical Description

In classical mechanics, the motion of celestial bodies such as planets and stars can be described using Newton's laws of motion and the law of universal gravitation. The motion of three mutually interacting bodies, known as the three-body problem, is a classic problem in physics and astronomy.

In this problem, we consider the gravitational interaction between three massive bodies: the Sun, Earth, and Jupiter. Each body exerts a gravitational force on the other bodies, causing them to accelerate according to Newton's second law of motion, which states that the force acting on an object is equal to the mass of the object multiplied by its acceleration ($F = ma$).

The gravitational force between two bodies can be described by Newton's law of universal gravitation:

$F=G \frac{{m_1 m_2}}{{r^2}}$


where:
- $F$ is the gravitational force between the two bodies,
- $G$ is the gravitational constant,
- $m_1$ and $m_2$ are the masses of the two bodies, and
- $r$ is the distance between the centers of the two bodies.

The gravitational force causes the bodies to accelerate towards each other, resulting in changes in their velocities and positions over time. These changes can be described by a set of ordinary differential equations (ODEs) that govern the motion of the bodies in the system.

For the three-body problem, the ODEs that describe the motion of each body can be written as follows:

For the Sun:

1. Rate of change of $x_1$: $\frac{{dx_1}}{{dt}} = vx_1$
2. Rate of change of $y_1$: $\frac{{dy_1}}{{dt}} = vy_1$
3. Rate of change of $vx_1$: $\frac{{dvx_1}}{{dt}} = G \left( \frac{{m_2 (x_2 - x_1)}}{{r_{12}^3}} + \frac{{m_3 (x_3 - x_1)}}{{r_{13}^3}} \right)$
4. Rate of change of $vy_1$: $\frac{{dvy_1}}{{dt}} = G \left( \frac{{m_2 (y_2 - y_1)}}{{r_{12}^3}} + \frac{{m_3 (y_3 - y_1)}}{{r_{13}^3}} \right)$

For the Earth:

1. Rate of change of $x_2$: $\frac{{dx_2}}{{dt}} = vx_2$
2. Rate of change of $y_2$: $\frac{{dy_2}}{{dt}} = vy_2$
3. Rate of change of $vx_2$: $\frac{{dvx_2}}{{dt}} = G \left( \frac{{m_1 (x_1 - x_2)}}{{r_{21}^3}} + \frac{{m_3 (x_3 - x_2)}}{{r_{23}^3}} \right)$
4. Rate of change of $vy_2$: $\frac{{dvy_2}}{{dt}} = G \left( \frac{{m_1 (y_1 - y_2)}}{{r_{21}^3}} + \frac{{m_3 (y_3 - y_2)}}{{r_{23}^3}} \right)$

For Jupiter:

1. Rate of change of $x_3$: $\frac{{dx_3}}{{dt}} = vx_3$
2. Rate of change of $y_3$: $\frac{{dy_3}}{{dt}} = vy_3$
3. Rate of change of $vx_3$: $\frac{{dvx_3}}{{dt}} = G \left( \frac{{m_1 (x_1 - x_3)}}{{r_{31}^3}} + \frac{{m_2 (x_2 - x_3)}}{{r_{32}^3}} \right)$
4. Rate of change of $vy_3$: $\frac{{dvy_3}}{{dt}} = G \left( \frac{{m_1 (y_1 - y_3)}}{{r_{31}^3}} + \frac{{m_2 (y_2 - y_3)}}{{r_{32}^3}} \right)$


where:
- $(x_1, y_1)$, $(x_2, y_2)$, and $(x_3, y_3)$ are the positions of the Sun, Earth, and Jupiter, respectively,
- $(vx_1, vy_1)$, $(vx_2, vy_2)$, and $(vx_3, vy_3)$ are the velocities of the Sun, Earth, and Jupiter, respectively,
- $G$ is the gravitational constant,
- $m_1$, $m_2$, and $m_3$ are the masses of the Sun, Earth, and Jupiter, respectively, and
- $r_{12}$, $r_{13}$, $r_{21}$, $r_{23}$, $r_{31}$, and $r_{32}$ are the distances between the bodies, calculated as the Euclidean distance between their positions.

To solve the three-body problem numerically, we use numerical integration techniques such as the Runge-Kutta method or the scipy.integrate.odeint function in Python. By integrating the differential equations over time, we can simulate the motion of the bodies and observe their trajectories as they interact with each other.

### Contents

- `gravitational_system.py`: Contains the function `derivs` for computing the derivatives of position and velocity. This file encapsulates the mathematical model of the gravitational system, providing the necessary functions to calculate the derivatives required for numerical integration.

- `plot_animation.py`: Contains the code for plotting trajectories and creating the animation. This file defines functions to visualize the simulation results, including plotting trajectories of the bodies over time and creating an animated GIF to represent the motion of the system.

- `three_body_simulation.py`: Main script to run the simulation and generate the animation. This file serves as the entry point for the simulation, where the initial conditions are set, the differential equations are solved using numerical integration, and the animation is generated based on the simulation results.

- `README.md`: This file, containing information about the project. It provides an overview of the project, instructions for installation and usage, details about the mathematical description of the problem, and information about the contents of the repository.

### Installation

1. Clone this repository:

```
git clone https://github.com/your-username/three-body-simulation.git
```

2. Navigate to the project directory:

```
cd three-body-simulation
```

3. Install the required dependencies (NumPy and Matplotlib):

```
pip install numpy matplotlib
```

### Usage

To run the simulation and generate the animation, execute the `three_body_simulation.py` script:

```
python three_body_simulation.py
```

The animation will be saved as `solar_system.gif` in the current directory.

