from __future__ import division, print_function  # python 2 to 3 compatibility
import matplotlib.pyplot as plt
from numpy import shape


def read_image(path_to_file):
    image = plt.imread(path_to_file)
    plt.imshow(image)

    print()

    plt.show()


if __name__ == "__main__":

    image_location = "/home/peter/Documents/streak_image_analysis/streak_test_image.png"
    read_image(image_location)
