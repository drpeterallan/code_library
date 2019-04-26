"""
----------------------
Title
----------------------

Brief description of script

:Date: """

import matplotlib.pyplot as plt
import numpy as np


def main():
    """ Python script template

    Parameters
    ----------
    Inputs: int/float/list/ndarray
        description

    Returns
    -------
    Outputs: int/float/list/ndarray
        description

    """

    return None


if __name__ == "__main__":
    main()

    a = np.linspace(10, 20, 10)
    b = np.linspace(1, 20, 10)

    lowest = map(min, a, b)
    print(list(lowest))

    def squared(n):
        return n * n

    print(list(map(squared, [2, 3, 6])))
    print(list(map(lambda i: i * i, [2, 3, 6])))
