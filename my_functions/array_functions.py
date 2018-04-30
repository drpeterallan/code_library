from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import argmin


def search_function(array_to_search, search_value):
    # Return index position of search_value in array_to_search
    return argmin(abs(array_to_search - search_value))