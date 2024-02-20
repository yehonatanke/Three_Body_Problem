import numpy as np
import pylab as py
from matplotlib import animation

# Define constants and initial conditions
Me = 6e24  # Mass of Earth in kg
Ms = 2e30  # Mass of Sun in kg
Mj = 1.9e27  # Mass of Jupiter in kg
G = 6.673e-11  # Gravitational Constant
RR = 1.496e11  # Normalizing distance in km (= 1 AU)
MM = 6e24  # Normalizing mass
TT = 365 * 24 * 60 * 60.0  # Normalizing time (1 year)
GG = (MM * G * TT ** 2) / (RR ** 3)  # Gravitational constant in normalized units


def force_es(r):
    """
    Calculates the gravitational force exerted on Earth by the Sun.
    
    Parameters:
    r (numpy.ndarray): Position vector of Earth.
    
    Returns:
    numpy.ndarray: Gravitational force vector exerted on Earth.
    """
    F = np.zeros(2)
    Fmag = GG * Me * Ms / (np.linalg.norm(r) + 1e-20) ** 2
    theta = np.arctan2(np.abs(r[1]), np.abs(r[0]) + 1e-20)
    F[0] = -Fmag * np.cos(theta) if r[0] > 0 else Fmag * np.cos(theta)
    F[1] = -Fmag * np.sin(theta) if r[1] > 0 else Fmag * np.sin(theta)
    return F


def force_js(r):
    """
    Calculates the gravitational force exerted on Jupiter by the Sun.
    
    Parameters:
    r (numpy.ndarray): Position vector of Jupiter.
    
    Returns:
    numpy.ndarray: Gravitational force vector exerted on Jupiter.
    """
    F = np.zeros(2)
    Fmag = GG * Mj * Ms / (np.linalg.norm(r) + 1e-20) ** 2
    theta = np.arctan2(np.abs(r[1]), np.abs(r[0]) + 1e-20)
    F[0] = -Fmag * np.cos(theta) if r[0] > 0 else Fmag * np.cos(theta)
    F[1] = -Fmag * np.sin(theta) if r[1] > 0 else Fmag * np.sin(theta)
    return F


def force_ej(re, rj):
    """
    Calculates the gravitational force exerted on Earth by Jupiter.
    
    Parameters:
    re (numpy.ndarray): Position vector of Earth.
    rj (numpy.ndarray): Position vector of Jupiter.
    
    Returns:
    numpy.ndarray: Gravitational force vector exerted on Earth by Jupiter.
    """
    r = re - rj
    F = np.zeros(2)
    Fmag = GG * Me * Mj / (np.linalg.norm(r) + 1e-20) ** 2
    theta = np.arctan2(np.abs(r[1]), np.abs(r[0]) + 1e-20)
    F[0] = -Fmag * np.cos(theta) if r[0] > 0 else Fmag * np.cos(theta)
    F[1] = -Fmag * np.sin(theta) if r[1] > 0 else Fmag * np.sin(theta)
    return F


def force(r, planet, re, rj):
    """
    Calculates the net gravitational force acting on a planet.
    
    Parameters:
    r (numpy.ndarray): Position vector of the planet.
    planet (str): Name of the planet ('earth' or 'jupiter').
    re (numpy.ndarray): Position vector of Earth.
    rj (numpy.ndarray): Position vector of Jupiter.
    
    Returns:
    numpy.ndarray: Net gravitational force vector acting on the planet.
    """
    if planet == 'earth':
        return force_es(r) + force_ej(r, rj)
    if planet == 'jupiter':
        return force_js(r) - force_ej(r, re)


def dr_dt(t, r, v, planet, re, rj):
    """
    Calculates the derivative of the position vector.
    
    Parameters:
    t (float): Time.
    r (numpy.ndarray): Position vector.
    v (numpy.ndarray): Velocity vector.
    planet (str): Name of the planet ('earth' or 'jupiter').
    re (numpy.ndarray): Position vector of Earth.
    rj (numpy.ndarray): Position vector of Jupiter.
    
    Returns:
    numpy.ndarray: Derivative of the position vector.
    """
    return v


def dv_dt(t, r, v, planet, re, rj):
    """
    Calculates the derivative of the velocity vector.
    
    Parameters:
    t (float): Time.
    r (numpy.ndarray): Position vector.
    v (numpy.ndarray): Velocity vector.
    planet (str): Name of the planet ('earth' or 'jupiter').
    re (numpy.ndarray): Position vector of Earth.
    rj (numpy.ndarray): Position vector of Jupiter.
    
    Returns:
    numpy.ndarray: Derivative of the velocity vector.
    """
    F = force(r, planet, re, rj)
    if planet == 'earth':
        y = F / Me
    if planet == 'jupiter':
        y = F / Mj
    return y


def RK4Solver(t, r, v, h, planet, re, rj):
    """
    Performs a single step of the RK4 method to solve the differential equations.
    
    Parameters:
    t (float): Time.
    r (numpy.ndarray): Position vector.
    v (numpy.ndarray): Velocity vector.
    h (float): Time step.
    planet (str): Name of the planet ('earth' or 'jupiter').
    re (numpy.ndarray): Position vector of Earth.
    rj (numpy.ndarray): Position vector of Jupiter.
    
    Returns:
    numpy.ndarray: Updated position and velocity vectors.
    """
    k11 = dr_dt(t, r, v, planet, re, rj) 
    k21 = dv_dt(t, r, v, planet, re, rj)
    
    k12 = dr_dt(t + 0.5 * h, r + 0.5 * h * k11, v + 0.5 * h * k21, planet, re, rj)
    k22 = dv_dt(t + 0.5 * h, r + 0.5 * h * k11, v + 0.5 * h * k21, planet, re, rj)
    
    k13 = dr_dt(t + 0.5 * h, r + 0.5 * h * k12, v + 0.5 * h * k22, planet, re, rj)
    k23 = dv_dt(t + 0.5 * h, r + 0.5 * h * k12, v + 0.5 * h * k22, planet, re, rj)
    
    k14 = dr_dt(t + h, r + h * k13, v + h * k23, planet, re, rj)
    k24 = dv_dt(t + h, r + h * k13, v + h * k23, planet, re, rj)
    
    y0 = r + h * (k11 + 2. * k12 + 2. * k13 + k14) / 6.
    y1 = v + h * (k21 + 2. * k22 + 2. * k23 + k24) / 6.
    
    z = np.zeros([2, 2])
    z = [y0, y1]
    return z


# Initialization
ti = 0  # initial time = 0
tf = 120  # final time = 120 years
N = 100 * tf  # 100 points per year
t = np.linspace(ti, tf, N)  # time array from ti to tf with N points 
h = t[2] - t[1]  # time step (uniform)

KE = np.zeros(N)  # Kinetic energy
PE = np.zeros(N)  # Potential energy
AM = np.zeros(N)  # Angular momentum
AreaVal = np.zeros(N)

r = np.zeros([N, 2])  # position vector of Earth
v = np.zeros([N, 2])  # velocity vector of Earth
rj = np.zeros([N, 2])  # position vector of Jupiter
vj = np.zeros([N, 2])  # velocity vector of Jupiter

ri = np.array([1496e8 / RR, 0])  # initial position of Earth
rji = np.array([5.2, 0])  # initial position of Jupiter
vi = np.array([0, np.sqrt(Ms * GG / ri[0])])  # Initial velocity vector for Earth
vji = np.array([0, 13.06e3 * TT / RR])  # Initial velocity vector for Jupiter

# Initializing the arrays with initial values
t[0] = ti
r[0, :] = ri
v[0, :] = vi
rj[0, :] = rji
vj[0, :] = vji

KE[0] = 0.5 * Me * np.linalg.norm(vi) ** 2
PE[0] = -GG * Ms * Me / np.linalg.norm(ri)
AM[0] = Me * np.linalg.norm(ri) * np.linalg.norm(vi)

for i in range(0, N - 1):
    [r[i + 1, :], v[i + 1, :]] = RK4Solver(t[i], r[i, :], v[i, :], h, 'earth', rj[i, :], vj[i, :])
    [rj[i + 1, :], vj[i + 1, :]] = RK4Solver(t[i], rj[i, :], vj[i, :], h, 'jupiter', r[i, :], v[i, :])

    KE[i + 1] = 0.5 * Me * np.linalg.norm(v[i + 1, :]) ** 2
    PE[i + 1] = -GG * Ms * Me / np.linalg.norm(r[i + 1, :])
    AM[i + 1] = Me * np.linalg.norm(r[i + 1, :]) * np.linalg.norm(v[i + 1, :])
    AreaVal[i + 1] = 0.5 * np.abs(np.cross(r[i, :], r[i + 1, :]))

# Create a figure and axis for the animation
fig, ax = py.subplots()
ax.axis('square')
ax.set_xlim((-7.2, 7.2))
ax.set_ylim((-7.2, 7.2))
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ax.plot(0, 0, 'o', markersize=9, markerfacecolor="#FDB813", markeredgecolor="#FD7813")
line1, = ax.plot([], [], 'o-', color='#d2eeff', markevery=10000, markerfacecolor='#0077BE', lw=2)
line2, = ax.plot([], [], 'o-', color='#e3dccb', markersize=8, markerfacecolor='#f66338', lw=2, markevery=10000)
ttl = ax.text(0.24, 1.05, '', transform=ax.transAxes, va='center')

# Animation function to update plot for each frame
def animate(i):
    earth_trail = 40
    jupiter_trail = 200
    tm_yr = 'Elapsed time = ' + str(round(t[i], 1)) + ' years'
    ttl.set_text(tm_yr)
    line1.set_data(r[i:max(1, i - earth_trail):-1, 0], r[i:max(1, i - earth_trail):-1, 1])
    line2.set_data(rj[i:max(1, i - jupiter_trail):-1, 0], rj[i:max(1, i - jupiter_trail):-1, 1])
    return (line1, line2)


# Create animation
anim = animation.FuncAnimation(fig, animate, frames=4000, interval=5, blit=True)

# Save animation as a GIF
anim.save('orbit_animation.gif', writer='pillow')

# Display animation
py.show()
