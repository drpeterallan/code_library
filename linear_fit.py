from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import linspace, polyfit, polyval, sqrt, diag
from random import random
import matplotlib.pyplot as plt


def linear_fit(x_array, y_array, plotting=False):

    """
    :param x_array:
    :param y_array:
    :param plotting:
    :return:
    """

    # Perform fit to the data
    coefs, cov = polyfit(x_array, y_array, 1, cov=True)

    # Compute fitting errors
    gradient, intercept = coefs
    gradient_error, intercept_error = sqrt(diag(cov))

    if plotting:

        # Create fit line
        x_fit = linspace(0, 10, 10)
        y_fit = polyval(coefs, x_fit)

        # Plot the data and the fit
        plt.plot(x_array, y_array, "bo", label="Data")
        plt.plot(x_fit, y_fit, "r-", lw=2, label="Fit")

        # Plot formatting etc.
        plt.xlabel("x", fontsize=16)
        plt.ylabel("y", fontsize=16)
        plt.legend(loc="upper left")
        plt.title("m = " + str(round(gradient, 3)) + " +/- " + str(round(gradient_error, 3))
                  + "\n"
                  + "c = " + str(round(intercept, 3)) + " +/- " + str(round(intercept_error, 3)))
        plt.show()


if __name__ == "__main__":

    # Create data to fit
    x_data = linspace(0, 10, 10)
    y_data = [random() for _ in range(len(x_data))]

    linear_fit(x_data, y_data, plotting=True)
