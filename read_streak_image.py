from __future__ import division, print_function  # python 2 to 3 compatibility
import matplotlib.pyplot as plt
from numpy import shape, array, random
from my_functions.pa3 import search_function


def read_image(path_to_file):

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
    plt.show()


def get_yaxis_lineout(y_axis, pixel_vals, y_lineout_position):

    # Function to get a lineout in the y axis
    # Search y_axis for user requested position
    y_index_pos, _ = search_function(y_axis, y_lineout_position)
    return pixel_vals[y_index_pos, :]


if __name__ == "__main__":

    # Get and read in the image data
    image_location = "/home/peter/Documents/streak_image_analysis/streak_test_image.png"
    time, space, data = read_image(image_location)

    # Plot the image - its inverted in
    # contour_image_plot(time, space, data)

    # Pull a lineout from the image
    # TODO: select max and min y positions and loop over lineouts in this region
    lineout_vals = get_yaxis_lineout(space, data, 200)
    plt.plot(time, lineout_vals)
    plt.show()

    # Find the 90 and 10% positions, or fit a sigmoid? Find slope centre and look for 90
    # and 10% around that

