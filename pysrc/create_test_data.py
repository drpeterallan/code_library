import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    """
    Generate random linearly increasing sudo data with error bars
    """

    # Create the data
    x_data = np.linspace(0, 10, 200)
    noise_std_dev = 5
    y_data = 10 + np.copy(x_data)**2 + np.random.normal(0.0, noise_std_dev, len(x_data))
    y_data_error = np.random.uniform(1.0, 5.5, len(x_data))

    # Visual check
    plt.errorbar(x_data, y_data, y_data_error, fmt="o")
    plt.show()

    # Save data to text file
    np.savetxt("/Users/pallan/Documents/neutron_bayesian_work/test_fitting_data_2nd_order.txt",
               np.transpose([x_data, y_data, y_data_error]),
               fmt="%.3e", delimiter="\t", header="x [a.u.]\ty [a.u.]\ty_error [a.u.]")