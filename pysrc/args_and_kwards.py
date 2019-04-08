"""
-----------------------
Args and kwargs example
-----------------------

Function to demonstrate the use of args and kwargs

:Date: 08/04/19
"""


def print_everything(a, b, *args, **kwargs):

    # Can pass conventional function arguments
    print(a, ", ", b)

    # Can pass an arbitrary number of args
    for count, argument in enumerate(args):
        print("{0}: {1}".format(count, argument))

    # Can pass an arbitrary number of arguments with keywords, stored as a dictionary
    for count, argument in enumerate(kwargs):
        print("{0}: {1}".format(count, argument))  # Returns variable name
    for i in kwargs:
        print(i, kwargs[i])  # Returns value
    print(kwargs["test1"])  # Index like a dictionary


if __name__ == "__main__":

    print_everything(1, 2, 3, 4, "Test", "Hello", [1, 2, 3], test1="string 1", test2="string 2")
