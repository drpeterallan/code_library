from matplotlib import cm
from numpy import arange
import matplotlib.pyplot as plt

# Create a list of colours from a colour map
cmap = cm.get_cmap("hsv")
colours = []
for i in arange(0.01, 0.9, 0.1):
    colours.append(cmap(i))

x = arange(0, 10, 0.1)
y = x**2

for i in range(len(colours)):
    plt.plot(x, y, color=colours[i], lw=2)
    y += 2
plt.show()

# Alternatively define a colour list

cmap = ["r", "b", "g", "k", "c"]

x = arange(0, 10, 0.1)
y = x**2

for i in range(len(cmap)):
    plt.plot(x, y, color=cmap[i], lw=2)
    y += 2
plt.show()