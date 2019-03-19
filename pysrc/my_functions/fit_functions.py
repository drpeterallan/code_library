from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import sqrt, log, exp


def linear_function(x_array, m, c):
    return m * x_array + c


def gaussian_function(x_array, height, centre, fwhm):
    c = fwhm / (2 * sqrt(2 * log(2)))
    return height * exp(-(x_array - centre)**2 / (2.0 * c**2.0))


def sigmoid_function(x_array, minimum, maximum, centre, slope):
    return minimum + ((maximum - minimum) / (1 + exp((centre - x_array) / slope)))

