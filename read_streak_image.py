from __future__ import division, print_function  # python 2 to 3 compatibility
import matplotlib.pyplot as plt
from numpy import shape, array, exp, arange, diag, sqrt, append, zeros
from my_functions.pa3 import search_function
from scipy.optimize import curve_fit


def read_image_file(path_to_file):
    # Function to read image file and return in format you would get real image
    # Read in image file and convert to a numpy array
    pixel_vals = array(plt.imread(path_to_file), dtype=float)
    pixel_vals = pixel_vals[::-1, :]  # Correct for reversal of data in y axis

    # Create time, and spatial axes
    image_len_x = shape(pixel_vals)[0]
    image_len_y = shape(pixel_vals)[1]
    x_axis = array(range(image_len_x))
    y_axis = array(range(image_len_y))

    return x_axis, y_axis, pixel_vals


def contour_image_plot(x_axis, y_axis, pixel_vals):
    # Function to plot data
    plt.contourf(x_axis, y_axis, pixel_vals, 50)
    plt.xlabel("Time")
    plt.ylabel("Space")


def get_yaxis_lineout(y_axis, pixel_vals, y_lineout_position):
    # Function to get a lineout in the y axis
    # Search y_axis for user requested position
    y_index_pos, _ = search_function(y_axis, y_lineout_position)
    return pixel_vals[y_index_pos, :]


def sigmoid_func(x_array, minimum, maximum, centre, slope):
    return minimum + ((maximum - minimum) / (1 + exp((centre - x_array) / slope)))


def fit_edge_profile(x_array, y_array):

    # Find edge position
    coefs_int = [0.0, 1.0, 1.0, 1.0]  # Initial guess of parameters
    coefs, cov = curve_fit(sigmoid_func, x_array, y_array, coefs_int)
    errors = sqrt(diag(cov))

    return coefs, errors


if __name__ == "__main__":

    # Get and read in the image data
    image_location = "/home/peter/Documents/streak_image_analysis/streak_test_image.png"
    time, space, data = read_image_file(image_location)

    lineout_positions = arange(0, 450, 50)
    edge_times = []
    edge_times_errors = []

    for lineout_position in lineout_positions:

        # Pull a lineout from the image
        # TODO: select max and min y (event clicker) and loop over lineouts in this region
        lineout_vals = get_yaxis_lineout(space, data, lineout_position)

        # Find the edge by fitting a sigmoid
        coefs, errors = fit_edge_profile(time, lineout_vals)
        edge_times.append(coefs[2])
        edge_times_errors.append(errors[2])

        # Plot data and fit
        # plt.plot(time, lineout_vals, "b-", lw=2)
        # y_fit = sigmoid_func(time, coefs[0], coefs[1], coefs[2], coefs[3])
        # plt.plot(time, y_fit, "r-", lw=1)
        # plt.title(coefs[2])
        # plt.show()

    edge_times = array(edge_times, dtype=float)
    edge_times_errors = array(edge_times_errors, dtype=float) * 10

    # Plot the image
    contour_image_plot(time, space, data)
    plt.errorbar(edge_times, lineout_positions, xerr=edge_times_errors, lw=0)
    plt.show()

    plt.errorbar(edge_times, lineout_positions, fmt="o", xerr=edge_times_errors, lw=0)
    plt.show()

