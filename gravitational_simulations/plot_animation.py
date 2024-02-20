# plot_animation.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot_animation(state):
    # Plot the trajectories and save each frame
    fig, ax = plt.subplots()
    ax.set_xlim(-2e11, 2e11)
    ax.set_ylim(-2e11, 2e11)
    line1, = ax.plot([], [], 'o-', label='Sun')
    line2, = ax.plot([], [], 'o-', label='Earth')
    line3, = ax.plot([], [], 'o-', label='Jupiter')

    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        line3.set_data([], [])
        return line1, line2, line3

    def update(frame):
        line1.set_data(state[:frame, 0], state[:frame, 1])
        line2.set_data(state[:frame, 4], state[:frame, 5])
        line3.set_data(state[:frame, 8], state[:frame, 9])
        return line1, line2, line3

    ani = FuncAnimation(fig, update, frames=len(state), init_func=init, blit=True)
    ani.save('solar_system.gif', writer='pillow', fps=30)

    plt.show()
