from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import array, copy, concatenate, shape, zeros
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from random import uniform


if __name__ == "__main__":

    num_particles = 100

    # Initialise particle positions
    x_pos = zeros(int(num_particles))
    y_pos = copy(x_pos)
    z_pos = copy(y_pos)

    # Create velocity array
    v_x = array([uniform(-1, 1.0) for i in range(len(x_pos))])
    v_y = array([uniform(-1, 1.0) for i in range(len(x_pos))])
    v_z = array([uniform(-1, 1.0) for i in range(len(x_pos))])

    # Initialise timings
    t = 0.0  # initial time
    t_fin = 14.0
    t_inc = 1.0

    # Loop over particles and update position
    while t < t_fin:
        x_pos = v_x * t
        y_pos = v_y * t
        z_pos = v_z * t
        t += t_inc

    plot_detector_x = [10, 8, 8, 10, 10]
    plot_detector_y = [-5, -5, 5, 5, -5]
    plot_detector_z = [5, 10, 10, 5, -5]

    # Plot data
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    for i in range(len(x_pos)):
        x_plot = [0.0, x_pos[i]]
        y_plot = [0.0, y_pos[i]]
        z_plot = [0.0, z_pos[i]]
        ax.plot3D(x_plot, y_plot, z_plot, color="red")
        ax.set_xlabel("x axis")
        ax.set_ylabel("y axis")
        ax.set_zlabel("z axis")
    ax.plot3D(plot_detector_x, plot_detector_y, plot_detector_z, "k-", lw=2)
    plt.show()

