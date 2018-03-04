from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import exp, arange, sqrt, log, array
import matplotlib.pyplot as plt


def gaussian_function(x_array, height, centre, fwhm):
    c = fwhm / (2 * sqrt(2 * log(2)))
    return height * exp(-(x_array - centre)**2 / (2.0 * c**2.0))


def test_mask(width, height, x_array):
    # Create a square pulse to convolve with a gaussian
    x_square = array([2 * -width, -width, -width, width, width, 2 * width], dtype=float)
    y_square = array([0, 0, 10, 10, 0, 0], dtype=float)
    return x_square, y_square


if __name__ == "__main__":

    # Create a gaussian
    x_gauss = arange(-15, 16, 0.1)
    y_gauss = gaussian_function(x_gauss, 10, 0, 5)

    # Create a square pulse to convolve
    x_square, y_square = test_mask(5, 10, x_gauss)
    plt.plot(x_square, y_square, "r-")

    plt.plot(x_gauss, y_gauss, "b-")
    plt.xlim(-11, 11)
    plt.ylim(-1, 11)
    plt.show()
