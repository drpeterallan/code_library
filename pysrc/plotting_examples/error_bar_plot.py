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
    y_error = np.random.uniform(1.0, 1.5, len(x)) * 10

    # Setup plotting
    set_rc_params()
    _, ax = plt.subplots(1, 1, figsize=(5, 4))

    # Plot the data
    ax.errorbar(x, y, yerr=y_error, ecolor="r", capsize=5, marker="o", color="r", lw=0, elinewidth=2)

    # Finish up
    ax.set_xlabel("x axis [units]")
    ax.set_ylabel("y axis [units]")
    plt.tight_layout()
    plt.show()
