from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import linspace, polyfit, polyval
from random import random
import matplotlib.pyplot as plt


def polynomial_fitting():

    # Create data to fit
    x_array = linspace(0, 10, 10)
    y_array = [random() for _ in range(len(x_array))]

    # Perform fit to the data
    poly_order = 1
    coefs, cov = polyfit(x_array, y_array, poly_order, cov=True)
    x_fit = linspace(0, 10, 10)
    y_fit = polyval(coefs, x_fit)

    # Plot the data and the fit
    plt.plot(x_array, y_array, "bo")
    plt.plot(x_fit, y_fit, "r-", lw=2)

    # Plot formatting
    plt.xlabel("x", fontsize=16)
    plt.ylabel("y", fontsize=16)
    plt.show()


if __name__ == "__main__":

    polynomial_fitting()
