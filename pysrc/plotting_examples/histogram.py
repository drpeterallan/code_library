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


if __name__ == "__main__":

    # Setup plotting defaults
    # set_rc_params()

    # Generate and plot data
    data = generate_data()
    plt.hist(data, bins="auto", facecolor="cornflowerblue", edgecolor="black")
    plt.show()

    # Use numpy
    # y_hist, bin_edges = np.histogram(data, bins="auto", range=None, weights=None, density=None)
    # print(bin_edges)
    # plt.bar(bin_edges[1:], y_hist)
    # print(len(y_hist), len(bin_edges))
    # # plt.plot(y_hist)
    # plt.show()