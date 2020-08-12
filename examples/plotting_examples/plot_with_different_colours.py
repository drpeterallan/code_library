"""
---------------------------
plot with different colours
---------------------------

Example of plotting with different colours

:Date: 02/05/19
"""

import matplotlib.pyplot as plt
import numpy as np
from esp.pysrc.utils.matplotlibrc_setup import set_rc_params
from matplotlib import cm


if __name__ == "__main__":

    # Create a list of random colours from a colour map
    cmap = cm.get_cmap("jet")
    colours = [cmap(i) for i in np.arange(0.01, 0.9, 0.1)]

    # Generate some data to plot in different colours
    x = np.arange(0, 10, 0.1)
    y = x**2

    # Setup plotting defaults and plot space
    set_rc_params()
    _, ax = plt.subplots(1, 2, sharey=True, sharex=True, figsize=(8, 4))

    # Loop over the colour platte and plot
    for i in range(len(colours)):
        ax[0].plot(x, y, color=colours[i], lw=2)
        y += 4  # offset plots

    # -------------------------------------------------

    # Alternatively manually define a colour list
    colours = ["blue", "red", "green", "goldenrod", "purple", "magenta", "cyan", "black"]

    # Loop over colours list and plot
    for i in range(len(colours)):
        ax[1].plot(x, y, color=colours[i], lw=2)
        y += 4

    # Finish up
    ax[0].set_title("CMAP", fontsize=12)
    ax[1].set_title("Manual", fontsize=12)
    plt.show()
