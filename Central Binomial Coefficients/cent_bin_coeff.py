#!/usr/bin/env pyhton3
from math import factorial


def central_bin_coeff(n: int) -> int:
    """Returns the n'th Central binomial coefficient as passed
        by the user.

    parameters:
        n [int]: The user passed n'th coefficent request.

    returns:
        [int]: The Central binomial coefficient of the passed number (n).
    """
    return factorial(2 * n) // (factorial(n)) ** 2


def main():
    for i in range(11):
        cbc: int = central_bin_coeff(i)
        print(f"{i}'th coefficient = {cbc}")


if __name__ == "__main__":
    main()

    # print(help(central_bin_coeff))

