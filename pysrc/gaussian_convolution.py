"""
----------------------
Gaussian Convolution
----------------------

Convolve gaussians of different FWHM with a single square pulse and plot results

:Date: 05/04/2019

"""

from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import arange, array, convolve, interp
import matplotlib.pyplot as plt
from python_code.pysrc.my_functions.fit_functions import gaussian_function
from python_code.pysrc.matplotlibrc_setup import set_rc_params


def test_mask(width, height, x_array):

    """ Function to create a square pulse and interpolate onto an array

    Parameters
    ----------
    width: int/float
        width of pulse in x axis
    height: int/float
        height of pulse in y axis
    x_array: list/ndarray
        list/array of x positions to interplate pulse onto

    Returns
    -------
    y_array: ndarray
        ndarray of interpolated y values for square pulse
    """

    # Create a square pulse to convolve with a gaussian
    x_square = array([2 * -width, -width, -width, width, width, 2 * width], dtype=float)
    y_square = array([0, 0, height, height, 0, 0], dtype=float)

    # Interpolate mask onto gaussian x grid
    y_array = interp(x_array, x_square, y_square)

    return y_array


if __name__ == "__main__":

    # Setting global plotting parameters
    set_rc_params()

    # Create a square pulse to convolve with a gaussian
    x_data = arange(-15, 16, 0.1)
    y_square = test_mask(5, 10, x_data)

    # Plot the initial unperturbed data
    plt.plot(x_data, y_square / max(y_square), "k-", label="Mask")

    # Loop over a range of different gaussian widths
    fwhms = [1, 2, 3, 4, 5]
    for fwhm in fwhms:

        # Create the gaussian to model the detector resolution
        y_gauss = gaussian_function(x_data, 10, 0, fwhm)

        # Do the convolution
        y_convolved = convolve(y_square, y_gauss, mode="same")

        # Plot the output
        plt.plot(x_data + 0.4, y_convolved / max(y_convolved), label=str(fwhm))

        # Finish up plot
        # plt.tick_params(axis="both", labelsize=16, pad=5)
        plt.xlabel("Position [a. u.]")
        plt.ylabel("Signal [a. u.]")
        plt.xlim(-12, 12)
        plt.ylim(0, 1.2)
        plt.legend(title="Gaussian FWHM:")

    plt.show()
