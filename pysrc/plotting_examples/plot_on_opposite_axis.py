"""
----------------------
plot on opposite axis
----------------------

Two lines plots on opposite y axes with the axis labels colour coded

:Date: """

import matplotlib.pyplot as plt
import numpy as np
from esp.pysrc.utils.matplotlibrc_setup import set_rc_params


if __name__ == "__main__":

    # Set plot format defaults
    set_rc_params()

    # Create some sudo data to plot
    x = np.linspace(0., 10., 100)
    y1 = 1000 / (x + 1)
    y2 = x ** 2

    # Plot data
    _, ax = plt.subplots()
    ax2 = ax.twinx()  # Create a 2nd axis to plot against
    ax.plot(x, y1, "b", label=r"$\rho$")
    ax.plot(0, 0, "r", label=r"$T_{\mathrm{E}}$")  # create an empty plot for labelling other axis plot
    ax2.plot(x, y2, "r")

    # Finish up
    ax.set_ylabel(r"$\rho$ [g/cc]", color="b")
    ax2.set_ylabel(r"$T_{\mathrm{E}}$ [K]", color="r")
    ax.set_xlabel("Time [s]")
    ax.legend(loc=(0.3, 0.5))
    plt.tight_layout()
    plt.show()
