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

    fig, ax = plt.subplots()
    ax.plot(energy_Al, intensity_Al, lw=2)

    # Plot formatting
    ax.tick_params(axis="both", labelsize=16, pad=5)
    # ax[0].set_xlim(-1.0, 1.1 * max(x_array))
    # ax[0].set_ylim(0.5 * min(y_array), 1.2 * max(y_array))
    ax.set_xlabel("Energy [eV]", fontsize=16)
    ax.set_ylabel(r"$I$ [10$^{-7}$ J/cm$^{2}$/s/Hz/srad]", fontsize=16)
    ax.legend(loc="upper left")
    plt.tight_layout(h_pad=2.0)
    plt.show()
    plt.show()

