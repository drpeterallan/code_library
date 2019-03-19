from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import linspace, copy
import matplotlib.pyplot as plt
from scipy.integrate import trapz


if __name__ == "__main__":

    # Create some test data to integrate over
    x = linspace(0, 10, 10)
    y = copy(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    print(trapz(y, x))

    plt.show()
