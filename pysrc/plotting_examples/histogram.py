"""
----------------------
Histogram example
----------------------

Example of a histogram plot

:Date: 12/04/19
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from python_code.pysrc.utils.matplotlibrc_setup import set_rc_params


def generate_data():
    """ Generate some random data with a Beta distribution

    Returns
    -------
    Outputs: ndarray
        beta distribution values

    """

    np.random.seed(123)
    number_of_points = int(1e4)
    data = stats.beta.rvs(a=1, b=4, size=number_of_points)

    return data


def get_bin_positions(bin_edges):
    """ Take the bin edges and calculate

    :param bin_edges:
    :return:
    """


if __name__ == "__main__":

    # Setup plotting defaults
    set_rc_params()

    # Generate and plot data
    data = generate_data()
    # plt.hist(data, bins=10, facecolor="cornflowerblue", edgecolor="black", density=True)
    # plt.show()

    # Use numpy
    y_hist, bin_edges = np.histogram(data, bins=20, range=None, weights=None, density=True)
    for i in np.arange(1, len(bin_edges), 1):
        print(bin_edges[i] - bin_edges[i-1])
    plt.bar(bin_edges[:-1], y_hist, edgecolor="black", width=0.0438)
    plt.xlim(0, 1.1)
    plt.show()

    # Calculate area under PDF
    print(sum(y_hist * 0.0438))