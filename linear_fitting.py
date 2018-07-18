from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import linspace, polyval, sqrt, diag, array, argmin
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from random import random
import sys
from my_functions.fit_functions import linear_function
sys.dont_write_bytecode = True  # Don't generate .pyc file


def search_array(array_to_search, search_term):
    # Convert list to search into numpy array
    array_to_search = array(array_to_search)
    index_pos = argmin(abs(array_to_search - search_term))
    return index_pos


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

    # Compute fitting errors
    gradient, intercept = coefs
    gradient_error, intercept_error = sqrt(diag(cov))
    coefs_error = sqrt(diag(cov))

    # Create the fit line
    x_fit = linspace(min(x_array), max(x_array), 100)
    y_fit = polyval(coefs, x_fit)

    if plotting:
        
        fig, ax = plt.subplots(2, 1, figsize=(7, 10), sharex=True)

        # Plot the data and the fit
        ax[0].errorbar(x_array, y_array, yerr=y_array_errs, fmt="o", color="blue", label="Data")
        ax[0].plot(x_fit, y_fit, "r-", lw=2, label="Fit")

        # Generate the fit limits
        coefs_upper = coefs + coefs_error
        y_fit_upper = polyval(coefs_upper, x_fit)
        coefs_lower = coefs - coefs_error
        y_fit_lower = polyval(coefs_lower, x_fit)

        # Plot the error envelope of the fit
        ax[0].fill_between(x_fit, y_fit_lower, y_fit_upper, color="blue", alpha=0.2,
                           label="Error bounds")

        # Compute the plot residuals
        # Get the y_fit values at the corresponding data values
        y_fit_vals_at_data = []
        for i in range(len(x_data)):
            index_pos = search_array(x_fit, x_data[i])
            y_fit_vals_at_data.append(y_fit[index_pos])

        residuals = y_data - array(y_fit_vals_at_data)

        # Plot the residuals
        ax[1].plot(x_array, residuals, "b-", lw=2)

        # Add a zero line for reference
        residuals_zero_x = [-1.0, 1.2 * max(x_array)]
        residuals_zero_y = [0.0, 0.0]
        ax[1].plot(residuals_zero_x, residuals_zero_y, "k--", lw=2)

        # Plot formatting etc.
        ax[0].tick_params(axis="both", labelsize=16, pad=5)
        ax[1].tick_params(axis="both", labelsize=16, pad=5)
        ax[0].set_xlim(-1.0, 1.1 * max(x_array))
        ax[0].set_ylim(0.5 * min(y_array), 1.2 * max(y_array))
        ax[1].set_ylim(-1.1, 1.1)
        ax[1].set_xlabel("x [units]", fontsize=16)
        ax[0].set_ylabel("y [units]", fontsize=16)
        ax[1].set_ylabel("Residuals", fontsize=16)
        ax[0].legend(loc="upper left")
        ax[0].set_title("m = " + str(round(gradient, 3)) + " +/- " + str(round(gradient_error, 3))
                        + "\n"
                        + "c = " + str(round(intercept, 3)) + " +/- " + str(round(intercept_error, 3)))
        plt.tight_layout(h_pad=2.0)
        plt.show()

    return x_fit, y_fit, gradient, gradient_error, intercept, intercept_error


if __name__ == "__main__":

    # Create data for fitting
    x_data = linspace(0, 10, 10)
    y_data = [3.1, 4.7, 5.2, 4.5, 6.8, 6.1, 8.0, 7.7, 9.3, 10.1]
    y_data_errors = [random() for _ in range(len(x_data))]

    # Perform fit to data
    linear_fit(x_data, y_data, y_data_errors, plotting=True)
