from __future__ import division, print_function  # python 2 to 3 compatibility
from pandas import read_csv
import matplotlib.pyplot as plt


def get_flychk_data(path_to_file):
    data = read_csv(path_to_file, skiprows=2, delim_whitespace=True)
    energy = data.iloc[:, 0].values
    intensity = data.iloc[:, 1].values
    return energy, intensity


def eV_to_nm(input_array):
    return 1240.0 / input_array


if __name__ == "__main__":

    directory = "/home/peter/FLYCHK/Al/"
    file_name = "Al_500_2_1e-4_NLTE"

    energy_Al, intensity_Al = get_flychk_data(directory + file_name)

    # Convert to nm
    energy_Al_nm = eV_to_nm(energy_Al)

    fig, ax = plt.subplots()
    ax.plot(energy_Al_nm, intensity_Al, lw=2)

    # Plot formatting
    ax.tick_params(axis="both", labelsize=16, pad=5)
    ax.set_xlabel("Energy [nm]", fontsize=16)
    ax.set_ylabel(r"$I$ [10$^{-7}$ J/cm$^{2}$/s/Hz/srad]", fontsize=16)
    ax.legend(loc="upper left")
    plt.tight_layout(h_pad=2.0)
    plt.show()

