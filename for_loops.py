from __future__ import division, print_function  # python 2 to 3 compatibility
import time
import numpy as np
import sys


def print_execution_time(start_time):
    print("Execution time = " + str(time.time() - start_time))


def run_for_loops():

    # Series of different for loop implementations and their performance

    # Number to loop over
    num = 5E6

    # --------------------------------------------------------------------------

    # First method - simple for loop and append to empty array

    start_time = time.time()
    squares1 = []
    for i in xrange(1, int(num)):
        squares1.append(i**2)
    print("Method 1:")
    print_execution_time(start_time)

    # --------------------------------------------------------------------------

    # Second method - list comprehension method

    start_time = time.time()
    squares2 = [i**2 for i in xrange(1, int(num))]
    print("Method 2:")
    print_execution_time(start_time)

    # --------------------------------------------------------------------------

    # Third method - append to a numpy array

    start_time = time.time()
    squares3 = np.zeros(len(squares1) + 1, dtype=float)
    for i in xrange(1, int(num)):
        squares3[i] = i**2
    print("Method 3:")
    print_execution_time(start_time)

    # --------------------------------------------------------------------------

    # Fourth method - use numpy arange
    # Fastest method

    start_time = time.time()
    squares4 = (np.arange(1, int(num)))**2
    print("Method 4:")
    print_execution_time(start_time)

    # --------------------------------------------------------------------------

    # Fifth method - use map and lambda function

    start_time = time.time()
    squares5 = map(lambda x: x ** 2, np.arange(1, int(num)))
    print("Method 5:")
    print_execution_time(start_time)

    # --------------------------------------------------------------------------

    # Get physical size of arrays
    print("1.", str(sys.getsizeof(squares1) / 1E6), "Mb", type(squares1))
    print("2.", str(sys.getsizeof(squares2) / 1E6), "Mb", type(squares2))
    print("3.", str(sys.getsizeof(squares3) / 1E6), "Mb", type(squares3))
    print("4.", str(sys.getsizeof(squares4) / 1E6), "Mb", type(squares4))
    print("5.", str(sys.getsizeof(squares5) / 1E6), "Mb", type(squares5))

    # Get length of arrays
    print(len(squares1))
    print(len(squares2))
    print(len(squares3))
    print(len(squares4))
    print(len(squares5))


if __name__ == "__main__":

    run_for_loops()
