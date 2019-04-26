"""
----------------------
Gaussian Convolution
----------------------

Convolve gaussians of different FWHM with a square pulse and plot results

:Date: 05/04/2019

"""

import numpy as np
import matplotlib.pyplot as plt
from python_code.pysrc.utils.fit_functions import gaussian_function
from python_code.pysrc.utils.matplotlibrc_setup import set_rc_params


def create_test_mask(width, height, x_array):

    """ Function to create a square pulse. This uses numpy 1D linear interpolation

    Parameters
    ----------
    width: int/float
        width of pulse in x axis
    height: int/float
        height of pulse in y axis
    x_array: list/ndarray
        list/array of x positions to interpolate pulse onto

    Returns
    -------
    y_array: ndarray
        ndarray of interpolated y values for square pulse
    """

    # Create a square pulse to convolve with a gaussian
    x_square = np.array([2 * -width, -width, -width, width, width, 2 * width], dtype=float)
    y_square = np.array([0, 0, height, height, 0, 0], dtype=float)

    # Interpolate mask onto x array
    return np.interp(x_array, x_square, y_square)


if __name__ == "__main__":

    # Setting global plotting parameters
    set_rc_params()

    # Create a square pulse to convolve with a gaussian
    x_data = np.arange(-15, 16, 0.1)
    y_square = create_test_mask(5, 10, x_data)

    # Setup plotting and plot unperturbed signal
    _, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.plot(x_data, y_square / max(y_square), label="Mask")

    # Loop over a range of different gaussian widths
    fwhms = [1, 2, 3, 4, 5]
    for fwhm in fwhms:

        # Create the gaussian to model the detector resolution
        y_gauss = gaussian_function(x_data, 10, 0, fwhm)

        # Do the convolution
        y_convolved = np.convolve(y_square, y_gauss, mode="same")

        # Plot the output
        ax.plot(x_data, y_convolved / max(y_convolved), label=str(fwhm))

        # Setup axes
        ax.set_xlabel("Position [a. u.]")
        ax.set_ylabel("Signal [a. u.]")
        ax.set_xlim(-12, 12)
        ax.set_ylim(0, 1.2)

    # Finish up
    plt.tight_layout()
    plt.legend(title="Gaussian FWHM:", loc="upper right")
    plt.show()
