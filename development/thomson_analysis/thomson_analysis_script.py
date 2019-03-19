from __future__ import division, print_function
import numpy as np
import scipy.constants as spc
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy import ndimage
from scipy.optimize import curve_fit
from PIL import Image


# ----------------------------------------------------------------------------------------------------------------------

"""USER INPUTS"""

volts = 5.27e3  # total potential between plates in V

nx = 1e3
ny = 1.6e3

aperture = 200  # um
dist_tcc = 0.807  # m
dist_image = 0.3  # m
mag = dist_image / (dist_tcc - dist_image)
source_size = 40  # um

# Setup the ions
ion_q = 70.0  # ion charge in units of e
ion_m = 196.9666  # ion mass in units of amu

# Image you wish to analyse  - NEED TO GET AN IMAGE TO USE
inf_name = "s###_thomson.inf"
img_name = inf_name[:-4] + ".img"
save_name = inf_name[:-4] + "_PSL.tif"

newx0, newy0 = 2421, 996  # Neutral point, i.e. straight through
rot = 90.0  # degrees
xoff, yoff = -10, 0  # define x and y offsets for cropping image

fadetime = 67

# Define particle energies to loop over
energies = ion_m * np.append(np.arange(0.3e6, 1e6, 0.05e6), np.arange(1e6, 50e6, 0.05e6))

c = spc.speed_of_light

ds = 1e-3

mag_z = np.arange(0.0, 0.062, 0.002)
# Magntidue of the magnetic field - read in from text file
mag_z_vals = np.array((0.0, 0.25, 0.33, 0.465, 0.53, 0.612, 0.66, 0.7, 0.725, 0.735, 0.761, 0.768, 0.773, 0.775, 0.779,
                       0.782, 0.779, 0.775, 0.773, 0.768, 0.761, 0.735, 0.725, 0.7, 0.66, 0.612, 0.53, 0.465, 0.33,
                       0.25, 0.0))

# Create an interpolation function for mag field. Input position and returns magnitude of field at that point
b_field_model = interp1d(mag_z, mag_z_vals)

# x = np.arange(0, 10, 1)
# y = x**2.0
# interp1d_func = interp1d(x, y)
# test = interp1d_func(5)
# print(test)
# plt.plot(x, y)
# plt.show()


def b_field(z):
    if z <= 0.06:
        b_mag = b_field_model(z)
    else:
        b_mag = 0.0
    return b_mag



