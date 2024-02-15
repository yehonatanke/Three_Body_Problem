import numpy as np
import pylab as py
from matplotlib import animation

# Define constants and initial conditions
# (Constants and initial conditions are already defined in the original script)

# Define functions for differential equations, solvers, etc.
# (Functions are already defined in the original script)

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
    # Update position of Earth and Jupiter for current frame
    earth_trail = 40
    jupiter_trail = 200
    tm_yr = 'Elapsed time = ' + str(round(t[i], 1)) + ' years'
    ttl.set_text(tm_yr)
    line1.set_data(r[i:max(1, i - earth_trail):-1, 0], r[i:max(1, i - earth_trail):-1, 1])
    line2.set_data(rj[i:max(1, i - jupiter_trail):-1, 0], rj[i:max(1, i - jupiter_trail):-1, 1])
    return (line1, line2)


# Create animation
anim = animation.FuncAnimation(fig, animate, frames=4000, interval=5, blit=True)

# Display animation
py.show()
