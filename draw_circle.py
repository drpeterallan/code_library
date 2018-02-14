from __future__ import division, print_function  # python 2 to 3 compatibility
from numpy import linspace, pi, cos, sin
import matplotlib.pyplot as plt


def draw_circle(radius, x_centre, y_centre):

    """
        Function to draw a circle
        Equation of a circle (x-x_centre)**2 + (y-y_centre)**2 = r2

        Parameters
        ----------
        radius: float
            radius of circle
        x_centre: float
            x coordinate of circle centre
        y_centre: float
            y coordinate of circle centre

        Returns
        -------
        none
        """

    # Define angles in r-theta coordinates
    theta = linspace(0, 2 * pi, 100)

    # Compute x-y points
    x = radius * cos(theta) + x_centre
    y = radius * sin(theta) + y_centre

    # Plot the circle
    fig, ax = plt.subplots(1)
    ax.plot(x, y, "b-", lw=2)
    ax.set_aspect("equal")
    ax.set_xlim(0.9 * min(x), 1.1 * max(x))
    ax.set_ylim(0.9 * min(y), 1.1 * max(y))
    plt.show()


if __name__ == "__main__":

    draw_circle(0.1, 2.0, 3.0)
