from __future__ import division, print_function  # python 2 to 3 compatibility
import numpy as np
import matplotlib.pyplot as plt


def linear_function(x_array, gradient, intercept):
    """
    Linear function of the form y = mx + c

    Parameters
    ----------
    x_array (array): array of values to return function over
    gradient (int/float): gradient
    intercept (int/float): intercept

    Returns
    -------
    ndarray: result of a first order polynomial of the form mx + c
    """
    return np.polyval([gradient, intercept], x_array)


def gaussian_function(x_array, height, centre, fwhm):
    c = fwhm / (2 * np.sqrt(2 * np.log(2)))
    return height * np.exp(-(x_array - centre)**2 / (2.0 * c**2.0))


def sigmoid_function(x_array, minimum, maximum, centre, slope):
    return minimum + ((maximum - minimum) / (1 + np.exp((centre - x_array) / slope)))


def run_example(fit_type):
    if fit_type == "linear" or "Linear":
        x_array = np.linspace(0, 10)
        y_array = linear_function(x_array, 2, 5)
        plt.plot(x_array, y_array)
        plt.show()


if __name__ == "__main__":

    # Run example
    run_example(fit_type="linear")
    print(linear_function.__doc__)
