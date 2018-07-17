from __future__ import division, print_function  # python 2 to 3 compatibility
from pandas import read_csv
import matplotlib.pyplot as plt
from my_functions.fit_functions import gaussian_function
from numpy import convolve

def get_flychk_data(path_to_file):
    data = read_csv(path_to_file, skiprows=2, delim_whitespace=True)
    energy = data.iloc[:, 0].values
    intensity = data.iloc[:, 1].values
    return energy, intensity


def eV_to_nm(input_array):
    return 1240.0 / input_array


if __name__ == "__main__":

    directory = "/home/peter/FLYCHK/Ne/"
    file_name = "Ne_300_1e20_0.1_NLTE"

    energy, intensity = get_flychk_data(directory + file_name)

    # Convert to nm
    energy_Al_nm = eV_to_nm(energy_Al)

    fig, ax = plt.subplots()
    ax.semilogy(energy, intensity, lw=2)

    # Plot formatting
    ax.tick_params(axis="both", labelsize=16, pad=5)
    ax.set_xlabel("Energy [eV]", fontsize=16)
    ax.set_ylabel(r"$I$ [10$^{-7}$ J/cm$^{2}$/s/Hz/srad]", fontsize=16)
    ax.legend(loc="upper left")
    plt.tight_layout(h_pad=2.0)
    plt.xlim(800, 1500)
    plt.show()

    # Create the gaussian to model the detector resolution
    y_gauss = gaussian_function(energy, 10, 1500, 20)
    y_convolved = convolve(intensity, y_gauss, mode="same")

    plt.semilogy(energy-300, y_convolved)
    plt.xlim(800, 1500)
    plt.ylim(1e-0, max(y_convolved))
    plt.show()

