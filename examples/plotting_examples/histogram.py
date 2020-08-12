"""
----------------------
Histogram example
----------------------

Example of a histogram plot using numpy

:Date: 12/04/19
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from esp.pysrc.utils.matplotlibrc_setup import set_rc_params


def generate_data(a=1, b=1, number_of_points=1000):
    """ Generate data with a Beta distribution

    Parameters
    ----------
    a and b: int/float
        shape parameters
    number_of_points: int/float
        number of points to sample in distribution

    Returns
    -------
    Outputs: ndarray
        beta distribution values

    """

    np.random.seed(123)
    data = stats.beta.rvs(a=a, b=b, size=int(number_of_points))

    return data


if __name__ == "__main__":

    # Setup plotting defaults
    set_rc_params()

    # Generate sudo data
    data = generate_data(a=1, b=4, number_of_points=1e4)

    # Can plot with matplotlib but then don't have histogram data. Quick way to produce visualisation
    # plt.hist(data, bins=10, facecolor="cornflowerblue", edgecolor="black", density=True)
    # plt.show()

    # ------------------------------------------------------------------------------------------------------------------

    # Use numpy - have histogram values, use density=True and get a PDF from which you can take probability
    # intervals. Note, if bins aren't of optimum width PDF won't integrate to 1.
    y_hist, bin_edges = np.histogram(data, bins="auto", range=None, weights=None, density=True)
    bin_width = bin_edges[1] - bin_edges[0]

    # Plot result
    fig, ax = plt.subplots(1, 1)
    ax.bar(bin_edges[:-1], y_hist, edgecolor="black", width=bin_width)

    # Calculate area under PDF and annotate to plot
    ax.annotate("{:.5f}".format(sum(y_hist * bin_width)), xy=(0.8, 0.8), xycoords="axes fraction")

    # Finish up plot
    ax.set_xlim(0, 1.1)
    plt.show()
