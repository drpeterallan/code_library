"""
----------------------
Array Functions
----------------------

Brief description of script

:Date: 05/04/2019
"""

from __future__ import division, print_function  # python 2 to 3 compatibility
import numpy as np
import matplotlib.pyplot as plt
from python_code.pysrc.utils.matplotlibrc_setup import set_rc_params


def linear_interp(x_array, y_array, num_elems):

    """ Function to perform a linear interpolation

    Parameters
    ----------
    x_array: list/ndarray
        x values
    y_array: list/ndarray
        y_values
    num_elems: int
        number of elements in new interpreted array

    Returns
    -------
    x_interp: list/ndarray
        x values of new interpreted values
    y_interp: list/ndarray
        interpreted y values
    """

    x_interp = np.linspace(min(x_array), max(x_array), int(num_elems))
    y_interp = np.interp(x_interp, x_array, y_array)

    return x_interp, y_interp


def search_array(array_to_search, search_value):

    """ Function to search an array. Calculates absolute difference between a user given value and each element
     in the list and returns the index position of the minimum difference, i.e. the closest value

    Parameters
    ----------
    array_to_search: list/ndarray
        list you wish to search
    search_value: int/float
        value you wish to find in array

    Returns
    -------
    index position: int
        index position in list of value closest to search_value

    """
    # Search array and find index position
    index_position = np.argmin(abs(np.array(array_to_search) - search_value))

    return index_position


def run_examples():

    print("Search Array example\n--------------------")
    search_value = 0.73
    array_to_search = [0, 0.12, 0.56, 0.7, 0.98]
    index_position = search_array(array_to_search, search_value)
    print("Searching for " + str(search_value))
    print("Index position of value: " + str(index_position))
    print("Value found: " + str(array_to_search[index_position]))

    print("\nLinear interp example\n---------------------")
    # Create test data
    x_test = np.linspace(0, 10, 5)
    y_test = np.copy(x_test)

    # Do the interpolation
    x_test_interp, y_test_interp = linear_interp(x_test, y_test, 100)

    # Plotting
    set_rc_params()  # Set plot formatting
    plt.plot(x_test, y_test, "bo", label="Data")
    plt.plot(x_test_interp, y_test_interp, "r-", label="Interp Data")
    plt.legend()
    plt.show()


if __name__ == "__main__":

    run_examples()

