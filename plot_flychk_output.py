from __future__ import division, print_function  # python 2 to 3 compatibility
from pandas import read_csv
import matplotlib.pyplot as plt


def get_flychk_data(path_to_file):
    data = read_csv(path_to_file, skiprows=2, delim_whitespace=True)
    energy = data.iloc[:, 0].values
    intensity = data.iloc[:, 1].values
    return energy, intensity

if __name__ == "__main__":

    directory = "/home/peter/FLYCHK/Al/"
    file_name = "Al_500_2_1e-4_NLTE"

    energy_Al, intensity_Al = get_flychk_data(directory + file_name)

    plt.plot(energy_Al, intensity_Al)
    plt.show()