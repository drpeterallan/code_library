"""
----------------------
boxplot
----------------------

Box and whisker plot example

:Date: 30/04/19
"""

import matplotlib.pyplot as plt
import numpy as np
from python_code.pysrc.utils.matplotlibrc_setup import set_rc_params

if __name__ == "__main__":

    # Set the random seed to produce same data each time
    np.random.seed(42)

    # Create some sudo data with outliers
    x = np.linspace(-2, 2, 100)
    x = np.arange(-2, 2, 0.1)
    outliers = [-4.5, 7, 8, 7.5]
    data = np.concatenate((x, outliers))

    set_rc_params()
    _, ax = plt.subplots()
    plot_label = ["Data set 1"]
    ax.boxplot(data, labels=plot_label, whis=1.5, notch=True, bootstrap=10000, meanline=True, showmeans=True,
               patch_artist=True,
               flierprops=dict(marker="*", markerfacecolor="r", markeredgecolor="r"),
               medianprops=dict(linewidth=1.5, color="b"),
               meanprops=dict(linewidth=1.5),
               boxprops=dict(linewidth=1.5, color="k", facecolor="red", alpha=0.4),
               whiskerprops=dict(linewidth=1.5),
               capprops=dict(linewidth=1.5))
    plt.show()
