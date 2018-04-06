from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import sqrt, arange, array
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def circle_function(x_array, a, b, r):
    # Equation of a circle (x - a)^2 + (y - b)^2 = r^2
    # In cartesian coordinates this will return the +x/+y portion of the circle
    return sqrt(-a**2 + (2 * a * x_array) + r**2 - x_array**2) + b**2


def fit_circle(x_array, y_array):
    coefs_int = [0.0, 0.0, 20]  # Initial guess of parameters
    coefs, _ = curve_fit(circle_function, x_array, y_array, coefs_int)
    return coefs


if __name__ == "__main__":

    # Create some random data - did this by drawing a portion the circle and creating
    # points which fell close to it
    x_data = arange(0, 20, 2)
    y_data = array([21, 19, 20, 16, 17, 18, 15, 12, 9, 11])  # convert to numpy array

    # Plot the data
    plt.plot(x_data, y_data, "bo", label="data")

    # Perform fit to data
    coefs = fit_circle(x_data, y_data)

    # Create the fit line
    x_fit = arange(min(x_data), max(x_data), 0.1)
    y_fit = circle_function(x_fit, coefs[0], coefs[1], coefs[2])

    # Overplot fit
    plt.plot(x_fit, y_fit, "r-", lw=2, label="fit")

    # Plot formatting etc.
    plt.xlabel("x axis", fontsize=16)
    plt.ylabel("y axis", fontsize=16)
    plt.tick_params(axis="both", labelsize=16, pad=5)
    plt.legend(loc="lower left")
    plt.xlim(-1, 21)
    plt.ylim(5, 22)
    plt.show()
