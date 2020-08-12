"""
------------------------
Series of functions
------------------------

List of functions, mainly for fitting

:Date: 23/04/2019
"""

from __future__ import division, print_function  # python 2 to 3 compatibility
import numpy as np
import matplotlib.pyplot as plt
from esp.pysrc.utils.matplotlibrc_setup import set_rc_params


def linear_function(x_array, gradient, intercept):
    """
    Linear function of the form y = mx + c

    Parameters
    ----------
    x_array: list/ndarray
        array of values to return function over
    gradient: int/float
        gradient, m
    intercept: int/float
        intercept, c

    Returns
    -------
    ndarray: result of a first order polynomial of the form mx + c
    """
    return np.polyval([gradient, intercept], x_array)


def gaussian_function(x_array, height, centre, fwhm):
    # TODO: options for normalising and also plotting using FWHM or STDEV
    c = fwhm / (2 * np.sqrt(2 * np.log(2)))
    return height * np.exp(-(x_array - centre)**2 / (2.0 * c**2.0))


def sigmoid_function(x_array, minimum, maximum, centre, slope):
    """
    Sigmoid function of the form y = min + (max - min) / (1 + exp((centre - x) / slope))

    Parameters
    ----------
    x_array: list/ndarray
        array of values to return function over
    minimum: int/float
        minimum/base value curve asymptotes to
    maximum: int/float
        maximum value curve asymptotes to
    centre: int/float
        centre position of slope
    slope: int/float
        controls the steepness of the slope

    Returns
    -------
    ndarray: result of a sigmoid funtion
    """
    return minimum + ((maximum - minimum) / (1 + np.exp((centre - x_array) / slope)))


def run_example(fit_type):
    set_rc_params()
    if fit_type == "Linear":
        print(linear_function.__doc__)
        x_array = np.linspace(0, 10)
        y_array = linear_function(x_array, 2, 5)
        _, ax = plt.subplots()
        ax.plot(x_array, y_array)
        plt.show()
    elif fit_type == "Sigmoid":
        print(sigmoid_function.__doc__)
        x_array = np.linspace(-15, 15, 100)
        _, ax = plt.subplots()
        slopes = [0.1, 1, 2, 3]
        for slope in slopes:
            y_array = sigmoid_function(x_array, 0, 1, 0, slope)
            ax.plot(x_array, y_array, label=slope)
        # Finish up
        ax.legend(title="slope:", loc="lower right")
        ax.annotate("min", xy=(0.1, 0.1), xycoords="axes fraction")
        ax.annotate("max", xy=(0.8, 0.85), xycoords="axes fraction")
        ax.axvline(0, color="k", linestyle="--")
        ax.annotate("centre", xy=(0.55, 0.1), xycoords="axes fraction")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":

    # Run example
    run_example(fit_type="Sigmoid")
