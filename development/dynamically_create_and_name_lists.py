from __future__ import division, print_function  # python 2 to 3 compatibility


def main():
    pass


if __name__ == "__main__":
    main()

    # Creating lists

    test_list = ['A', 1, 2, 3, 'B', 4, 5, 6]

    g = globals()
    for i in range(len(test_list)):
        print
        'creating list'
        g['AAA_{}'.format(i)] = []

    print(g['AAA_1'])
