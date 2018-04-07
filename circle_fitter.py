from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import sqrt, arange, array
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def circle_function(x_array, a, b, r):
    # Equation of a circle (x - a)^2 + (y - b)^2 = r^2
    # In cartesian coordinates this will return the +x/+y portion of the circle
    return (-a**2 + (2 * a * x_array) + r**2 - x_array**2)**0.5 + b**2


def ellipse_function(x_array, a, b, x0, y0):
    return ((b * (a**2 + x_array**2 + (2 * x_array * x0 - x0**2))**0.5) / a) + y0


def ellipse_function2(x_array, a, b, x0, y0):
    return y0 - ((b * (a**2 + x_array**2 + (2 * x_array * x0 - x0**2))**0.5) / a)


def fit_circle(x_array, y_array):
    coefs_int = [0.0, 0.0, 20]  # Initial guess of parameters
    coefs, _ = curve_fit(circle_function, x_array, y_array, coefs_int)
    return coefs


def fit_ellipse(x_array, y_array):
    coefs_int = [1.0, 1.0, 0.0, 0.0]
    coefs, _ = curve_fit(ellipse_function, x_array, y_array, coefs_int)
    return coefs


if __name__ == "__main__":

    # Create some random data - did this by drawing a portion the circle and creating
    # points which fell close to it
    x_data = arange(0, 20, 2)
    y_data = array([21, 19, 20, 16, 17, 18, 15, 12, 9, 11])  # convert to numpy array

    # Plot the data
    plt.plot(x_data, y_data, "bo", label="data")

    # Perform fit to data
    coefs = fit_ellipse(x_data, y_data)
    print(coefs)

    # Create the fit line
    x_fit = arange(-100, max(x_data) + 100, 0.1)
    y_fit = ellipse_function(x_fit, coefs[0], coefs[1], coefs[2], coefs[3])
    y_fit2 = ellipse_function2(x_fit, coefs[0], coefs[1], coefs[2], coefs[3])

    # Overplot fit
    plt.plot(x_fit, y_fit, "r-", lw=2, label="fit")
    plt.plot(x_fit, y_fit2, "g-", lw=2, label="fit")

    # Plot formatting etc.
    plt.xlabel("x axis", fontsize=16)
    plt.ylabel("y axis", fontsize=16)
    plt.tick_params(axis="both", labelsize=16, pad=5)
    plt.legend(loc="lower left")
    # plt.xlim(-31, 31)
    # plt.ylim(5, 22)
    plt.show()
