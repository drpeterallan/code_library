from __future__ import division, print_function  # python 2 to 3 compatibility
import time
import numpy as np
import sys


def get_execution_time(start_time):
    return time.time() - start_time


def get_list_size(input_list):
    print(str(sys.getsizeof(input_list) / 1E6), "Mb", type(input_list), len(input_list))


def run_list_creation(elements_in_list):

    # Series of different for loop implementations and their performance

    execution_times = []

    # First method - simple for loop and append to empty array

    start_time = time.time()
    squares1 = []
    for i in xrange(1, int(elements_in_list)):
        squares1.append(i**2)

    print("Method 1:")
    ex_time1 = get_execution_time(start_time)
    print(ex_time1)
    execution_times.append(ex_time1)

    # --------------------------------------------------------------------------

    # Second method - list comprehension method

    start_time = time.time()
    squares2 = [i**2 for i in xrange(1, int(elements_in_list))]

    print("Method 2:")
    ex_time2 = get_execution_time(start_time)
    print(ex_time2)
    execution_times.append(ex_time2)

    # --------------------------------------------------------------------------

    # Third method - append to a numpy array

    start_time = time.time()
    squares3 = np.zeros(len(squares1), dtype=float)
    for i in xrange(1, int(elements_in_list) - 1):
        squares3[i] = i**2
    print("Method 3:")
    get_execution_time(start_time)

    # --------------------------------------------------------------------------

    # Fourth method - use numpy arange
    # Fastest method

    start_time = time.time()
    squares4 = (np.arange(1, int(elements_in_list)))**2
    print("Method 4:")
    get_execution_time(start_time)

    # --------------------------------------------------------------------------

    # Fifth method - use map and lambda function

    start_time = time.time()
    squares5 = map(lambda x: x ** 2, np.arange(1, int(elements_in_list)))
    print("Method 5:")
    get_execution_time(start_time)

    # --------------------------------------------------------------------------

    # Get physical size of arrays
    print("1.")
    get_list_size(squares1)
    print("2.")
    get_list_size(squares2)
    print("3.")
    get_list_size(squares3)
    print("4.")
    get_list_size(squares4)
    print("5.")
    get_list_size(squares5)


if __name__ == "__main__":

    elements_in_list = 1e3
    run_list_creation(elements_in_list)