from __future__ import division, print_function  # python 2 to 3 compatibility
from pandas import read_csv
import matplotlib.pyplot as plt
from numpy import convolve, interp, linspace


def get_flychk_data(path_to_file):
    data = read_csv(path_to_file, skiprows=2, delim_whitespace=True)
    # Returns energy, intensity
    return data.iloc[:, 0].values, data.iloc[:, 1].values


if __name__ == "__main__":

    # Get data
    directory = "/home/peter/FLYCHK/Al/"
    files = ["Al_500_2_1e-4_NLTE", "Al_500_2_1e-4_NLTE_emissivity"]

    for file in files:
        energy, intensity = get_flychk_data(directory + file)
        plt.semilogy(energy, intensity, label=file)
    plt.legend()
    plt.show()


