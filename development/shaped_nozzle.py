import matplotlib.pyplot as plt
from pysrc.my_functions.fit_functions import power_law
from numpy import linspace

def main():

    # All dimensions are in mm
    input_radius = 4.0
    exit_radius = 0.5
    length = 5
    max_x_pos = 1.5 * input_radius

    x_positions = [max_x_pos, input_radius, exit_radius, max_x_pos]
    y_positions = [0.0, 0.0, -length, -length]

    plt.plot(x_positions, y_positions, color="b", marker="o", lw=2)
    plt.show()

    # x_curve


if __name__ == "__main__":
    main()