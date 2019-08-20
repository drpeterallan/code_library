import pkg_resources
import numpy
import theano
import pymc3

if __name__ == "__main__":

    [print(library) for library in pkg_resources.working_set]

    print(numpy.__version__)
    print(theano.__version__)
    print(pymc3.__version__)