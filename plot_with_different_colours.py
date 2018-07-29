from __future__ import division, print_function  # python 2 to 3 compatibility
from matplotlib import cm
from numpy import arange
import matplotlib.pyplot as plt

# Create a list of colours from a colour map
cmap = cm.get_cmap("hsv")
colours = [cmap(i) for i in arange(0.01, 0.9, 0.1)]

# Generate some data to plot in different colours
x = arange(0, 10, 0.1)
y = x**2

for i in range(len(colours)):
    plt.plot(x, y, color=colours[i], lw=2)
    y += 2  # offset plots
plt.show()

# Alternatively manually define a colour list

colours = ["r", "b", "g", "k", "c"]

x = arange(0, 10, 0.1)
y = x**2

for i in range(len(colours)):
    plt.plot(x, y, color=colours[i], lw=2)
    y += 2
plt.show()
