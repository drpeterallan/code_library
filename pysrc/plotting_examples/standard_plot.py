"""
----------------------
Standard plot
----------------------

Example of simple data plot

:Date: 19/04/19
"""

import matplotlib.pyplot as plt
import numpy as np
from python_code.pysrc.utils.matplotlibrc_setup import set_rc_params


if __name__ == "__main__":

    # Generate some data to plot
    x = np.arange(0, 10)
    y = x**2

    # Setup plotting
    set_rc_params()
    _, ax = plt.subplots(1, 1, figsize=(5, 4))

    # Plot the data
    ax.plot(x, y, "bo")

    # Finish up
    ax.set_xlabel("x axis [units]")
    ax.set_ylabel("y axis [units]")
    plt.tight_layout()
    plt.show()
