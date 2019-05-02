from matplotlib import rcParams
import matplotlib.pyplot as plt
from numpy import arange


def set_rc_params():

    rcParams.update({"font.size": 14,
                     "font.family": "sans-serif",
                     "lines.linewidth": 1.5,
                     "xtick.labelsize": 14,
                     "xtick.major.size": 5,
                     "xtick.major.width": 1,
                     "xtick.major.pad": 10,
                     "ytick.labelsize": 14,
                     "ytick.major.size": 5,
                     "ytick.major.width": 1,
                     "image.cmap": "jet"
                     })


if __name__ == "__main__":

    # Set rc params
    set_rc_params()

    # Print all available options
    print(rcParams.items())

    # Plot some data to demo changed rcParams
    x = arange(0, 10)
    y = x * x
    _, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
