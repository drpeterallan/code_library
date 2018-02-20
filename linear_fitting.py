from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import linspace, polyval, sqrt, diag
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from random import random


def linear_function(x_array, m, c):
    return m * x_array + c


def linear_fit(x_array, y_array, y_array_errs, plotting=False):

    """
    Function to perform a linear fit to data and compute the fitting errors.

    Parameters
    ----------
    x_array: list or numpy array
        1D list of x data points
    y_array: list or numpy array
        1D list of y data points
    y_array_errs: list or numpy array
        1D list of y errors
    plotting: bool
        key word to turn on plotting and display results of fit to data

    Returns
    -------
    x_fit: numpy array
        1D array of x values which fit is computed over
    y_fit: numpy array
        1D array of fitted y values
    gradient: float
        the gradient of the fitted line
    gradient_error: float
        error in the gradient determined from the variance in the fit coefficient
    intercept: float
        y axis intercept
    intercept_error: float
          error in the intercept determined from the variance in the fit coefficient
    """

    # Perform fit to the data
    coefs_int = [0.0, 0.0]  # Initial guess of parameters
    coefs, cov = curve_fit(linear_function, x_array, y_array, coefs_int,
                           absolute_sigma=y_array_errs)

    """sigma or absolute sigma?"""

    # Compute fitting errors
    gradient, intercept = coefs
    gradient_error, intercept_error = sqrt(diag(cov))
    coefs_error = sqrt(diag(cov))

    # Create the fit line
    x_fit = linspace(min(x_array), max(x_array), 100)
    y_fit = polyval(coefs, x_fit)

    if plotting:

        # Plot the data and the fit
        plt.errorbar(x_array, y_array, yerr=y_array_errs, fmt="o", color="blue", label="Data")
        plt.plot(x_fit, y_fit, "r-", lw=2, label="Fit")

        # Generate the fit limits
        coefs_upper = coefs + coefs_error
        y_fit_upper = polyval(coefs_upper, x_fit)
        coefs_lower = coefs - coefs_error
        y_fit_lower = polyval(coefs_lower, x_fit)

        # Plot the error envelope of the fit
        plt.fill_between(x_fit, y_fit_lower, y_fit_upper, color="blue", alpha=0.2,
                         label="Error bounds")

        # Plot formatting etc.
        plt.tick_params(axis="both", labelsize=16, pad=5)
        plt.xlim(-1.0, 1.2 * max(x_array))
        plt.ylim(0.5 * min(y_array), 1.2 * max(y_array))
        plt.xlabel("x [units]", fontsize=16)
        plt.ylabel("y [units]", fontsize=16)
        plt.legend(loc="upper left")
        plt.title("m = " + str(round(gradient, 3)) + " +/- " + str(round(gradient_error, 3))
                  + "\n"
                  + "c = " + str(round(intercept, 3)) + " +/- " + str(round(intercept_error, 3)))
        plt.show()

    return x_fit, y_fit, gradient, gradient_error, intercept, intercept_error


if __name__ == "__main__":

    # Create data for fitting
    x_data = linspace(0, 10, 10)
    y_data = [3.1, 4.7, 5.2, 4.5, 6.8, 6.1, 8.0, 7.7, 9.3, 10.1]
    y_data_errors = [random() for _ in range(len(x_data))]

    # Perform fit to data
    linear_fit(x_data, y_data, y_data_errors, plotting=True)
