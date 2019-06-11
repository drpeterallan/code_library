"""
-----------------------------
Create a 2D pandas data frame
-----------------------------

Take multiple 1D arrays and concatenate into a single data frame

:Date: """

import numpy as np
import pandas as pd


if __name__ == "__main__":

    # Create arrays
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    row_indices = ["a", "b", "c"]
    column_indices = [27, 73]

    # Combine arrays into a 2d array
    c = np.vstack((a, b)).T

    # Create the data frame
    df = pd.DataFrame(data=c, index=row_indices, columns=column_indices)

    # Output results
    print(df)
    print(df.loc["a", 27])
    print(df.iloc[0, 0])  # Alternatively

