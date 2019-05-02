"""
----------------------
Contour plot
----------------------

Example of a filled contour plot with contour lines added

:Date: 02/05/19
"""

import matplotlib.pyplot as plt
import numpy as np
from python_code.pysrc.utils.matplotlibrc_setup import set_rc_params

if __name__ == "__main__":

    # Set default plot formats
    set_rc_params()

    # Set the
    np.random.seed(42)

    # Create some sudo data to plot
    x = np.linspace(0, 12, 7)
    y = np.array([0.5, 1, 2, 3, 5, 7], dtype=float)
    z = ([174, 161, 147, 132, 122, 111, 100],
         [167, 154, 141, 124, 111, 103, 101],
         [120, 113, 108,  88,  94,  81,  78],
         [83,   83,  74,  66,  59,  56,  51],
         [77,   71,  64,  58,  52,  47,  42],
         [76,   70,  64,  56,  53,  47,  43])

    # Create levels for colorbar
    min_z, max_z = np.amin(z), np.amax(z)
    levels = np.linspace(min_z, max_z, 8, dtype=int)

    # Plot the data
    fig, ax = plt.subplots()
    contour_plot = ax.contourf(x, y, z, 500)
    fig.colorbar(contour_plot, ax=ax, ticks=levels, pad=0.05)

    # Add contour lines with labels
    CS = ax.contour(x, y, z, colors="k")
    ax.clabel(CS, fontsize=10, inline=True, fmt="%1.2f")

    # Finish up
    plt.tight_layout()
    plt.show()