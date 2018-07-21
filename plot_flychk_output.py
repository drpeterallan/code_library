from __future__ import division, print_function  # python 2 to 3 compatibility
from pandas import read_csv
import matplotlib.pyplot as plt
from my_functions.fit_functions import gaussian_function
from numpy import convolve, interp, linspace


def get_flychk_data(path_to_file):
    data = read_csv(path_to_file, skiprows=2, delim_whitespace=True)
    # Returns energy, intensity
    return data.iloc[:, 0].values, data.iloc[:, 1].values


if __name__ == "__main__":

    # Get data
    directory = "/home/peter/FLYCHK/Ne/"
    file_name = "Ne_300_1e20_0.1_NLTE"
    energy, intensity = get_flychk_data(directory + file_name)

    # Interpolate the flychk spectra onto a regular grid
    energy_interp = linspace(min(energy), max(energy), 5e3)
    intensity_interp = interp(energy_interp, energy, intensity)

    # Create a gaussian to model the detector resolution/source broadening effects
    FWHM = 5
    mid_point = (min(energy_interp) + max(energy_interp)) / 2  # centre gaussian on spectrum
    y_gauss = gaussian_function(energy_interp, 1, mid_point, FWHM)
    y_convolved = convolve(intensity_interp, y_gauss, mode="same")

    # Plot the results
    # Raw spectrum
    fig, ax = plt.subplots(2, 1, figsize=(7, 10), sharex=True)
    ax[0].semilogy(energy, intensity, "b-", lw=2, label="FLYCHK")
    ax[0].tick_params(axis="both", labelsize=16, pad=5)
    ax[0].set_ylabel(r"$I$ [10$^{-7}$ J/cm$^{2}$/s/Hz/srad]", fontsize=16)

    # Convolved spectrum
    ax[1].semilogy(energy_interp, y_convolved, "r-", lw=2, label="Convolved (FWHM=" + str(FWHM) + ")")
    ax[1].tick_params(axis="both", labelsize=16, pad=5)
    ax[1].set_xlabel("Energy [eV]", fontsize=16)
    ax[1].set_ylabel(r"$I$ [10$^{-7}$ J/cm$^{2}$/s/Hz/srad]", fontsize=16)

    # Global params/finish up
    ax[1].legend(loc="upper right")
    ax[1].set_xlim(800, 1500)
    fig.tight_layout()
    plt.show()

