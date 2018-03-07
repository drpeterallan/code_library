from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import exp, arange, sqrt, log, array, convolve, interp
import matplotlib.pyplot as plt


def gaussian_function(x_array, height, centre, fwhm):
    c = fwhm / (2 * sqrt(2 * log(2)))
    return height * exp(-(x_array - centre)**2 / (2.0 * c**2.0))


def test_mask(width, height, x_array):

    # Create a square pulse to convolve with a gaussian
    x_square = array([2 * -width, -width, -width, width, width, 2 * width], dtype=float)
    y_square = array([0, 0, height, height, 0, 0], dtype=float)

    # Interpolate mask onto gaussian x grid
    y_square = interp(x_array, x_square, y_square)

    return y_square


if __name__ == "__main__":

    # Create a square pulse to convolve with a gaussian
    x_data = arange(-15, 16, 0.1)
    y_square = test_mask(5, 10, x_data)

    # Plot the initial unperturbed data
    plt.plot(x_data, y_square / max(y_square), "k-", lw=2, label="Mask")

    # Loop over a range of different gaussian widths
    fwhms = [1, 2, 3, 4, 5]
    for fwhm in fwhms:

        # Create the gaussian to model the detector resolution
        y_gauss = gaussian_function(x_data, 10, 0, fwhm)

        # Do the convolution
        y_convolved = convolve(y_square, y_gauss, mode="same")

        # Plot the output
        plt.plot(x_data + 0.4, y_convolved / max(y_convolved), lw=2, label=str(fwhm))

        # Finish up plot
        plt.tick_params(axis="both", labelsize=16, pad=5)
        plt.xlabel("Position [a. u.]", fontsize=16)
        plt.ylabel("Signal [a. u.]", fontsize=16)
        plt.xlim(-11, 11)
        plt.ylim(0, 1.2)
        plt.legend(title="Gaussian FWHM:", fontsize=12)

    plt.show()
