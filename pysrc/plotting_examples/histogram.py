"""
----------------------
Histogram example
----------------------

Example of a histogram plot

:Date: """

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from python_code.pysrc.utils.matplotlibrc_setup import set_rc_params

def generate_data():
    """ Generate some random data with a Beta distribution

    Returns
    -------
    Outputs: int/float/list/ndarray
        description

    """

    np.random.seed(123)
    number_of_points = int(1e4)
    data = stats.beta.rvs(a=1, b=4, size=number_of_points)

    return data


if __name__ == "__main__":

    # Setup plotting defaults
    set_rc_params()

    # Generate and plot data
    data = generate_data()
    plt.hist(data, bins="auto")
    plt.show()
