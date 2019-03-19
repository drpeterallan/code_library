import numpy as np


def main(array1, array2):

    """
    Perform various checks on arrays

    Parameters
    ----------
    array1: int/float/array
    array2: int/float/array

    Returns
    -------
    None
    """

    print(len(array1), len(array2))
    # Firstly check arrays are of the same length
    assert array1.size == array2.size, "Arrays must have the same number of elements"


if __name__ == "__main__":

    # Create some data to check
    array1 = np.linspace(0, 10, 9)
    array2 = np.linspace(0, 20, 10)

    main(array1, array2)
