from __future__ import division, print_function  # python 2 to 3 compatibility
import time
import numpy as np
import sys


def get_execution_time(start_time):
    return time.time() - start_time


def get_list_properties(input_list):
    print((sys.getsizeof(input_list)), "bytes", type(input_list))


def run_list_creation(elements_in_list):

    """
    Series of different implementations for creating lists and execution times
    """

    # ------------------------------------------------------------------------------------------------------------

    # 1ST METHOD - for loop and append to empty array

    start_time = time.time()
    squares1 = []
    for i in range(1, int(elements_in_list)):
        squares1.append(i**2)

    # Get timing info
    print("Execution times" + "\n--------------------")
    print("Method 1:")
    ex_time1 = get_execution_time(start_time)
    print(ex_time1)

    # ------------------------------------------------------------------------------------------------------------

    # 2ND METHOD - list comprehension

    start_time = time.time()
    squares2 = [i**2 for i in range(1, int(elements_in_list))]

    print("Method 2:")
    ex_time2 = get_execution_time(start_time)
    print(ex_time2)

    # ------------------------------------------------------------------------------------------------------------

    # 3RD METHOD - for loop and append to a numpy array

    start_time = time.time()
    squares3 = np.zeros(len(squares1), dtype=float)
    for i in range(1, int(elements_in_list) - 1):
        squares3[i] = i**2

    print("Method 3:")
    ex_time3 = get_execution_time(start_time)
    print(ex_time3)

    # ------------------------------------------------------------------------------------------------------------

    # 4TH METHOD - use arange
    # Fastest method

    start_time = time.time()
    squares4 = (np.arange(1, int(elements_in_list)))**2
    print("Method 4:")

    ex_time4 = get_execution_time(start_time)
    print(ex_time4)

    # ------------------------------------------------------------------------------------------------------------

    # 5TH METHOD - use map and lambda function

    start_time = time.time()
    squares5 = list(map(lambda x: x ** 2, np.arange(1, int(elements_in_list))))

    print("Method 5:")
    ex_time5 = get_execution_time(start_time)
    print(ex_time5)
    print("\n")

    # ------------------------------------------------------------------------------------------------------------

    # Get physical size of arrays
    print("Array sizes and types" + "\n------------------------")
    print("Method 1:")
    get_list_properties(squares1)
    print("Method 2:")
    get_list_properties(squares2)
    print("Method 3:")
    get_list_properties(squares3)
    print("Method 4:")
    get_list_properties(squares4)
    print("Method 5:")
    get_list_properties(squares5)


if __name__ == "__main__":

    elements_in_list = 1e6
    run_list_creation(elements_in_list)

