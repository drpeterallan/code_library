"""
----------------------
Array Functions
----------------------

Brief description of script

:Date: 05/04/2019
"""

from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import argmin, array


def search_function(array_to_search, search_value):

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
    index_position = argmin(abs(array(array_to_search) - search_value))

    return index_position


def run_examples():

    # search_function example
    search_value = 0.73
    array_to_search = [0, 0.12, 0.56, 0.7, 0.98]
    index_position = search_function(array_to_search, search_value)
    print("Index position of value: " + str(index_position))
    print("Value found: " + str(array_to_search[index_position]))


if __name__ == "__main__":

    run_examples()

