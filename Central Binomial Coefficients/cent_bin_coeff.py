#!/usr/bin/env pyhton3
"""Script that returns the n'th Central binomial coefficient.
The requested n'th coefficient is passed to the central_bin_coeff(n)
function and the n'th coefficient is calculated and returned as an
integer. Function can use a try/except block for some lite error
checking if wanted or delete the try/except block and use the pure
return statement if error checking is not needed or wanted.

Formula: f(n) = (2n)!/(n!)^2 for all n >= 0

Written by:
Github: itsf4llofstars

For use in linux systems. Other OS's may need changes in code.
"""
import math


def central_bin_coeff(n) -> int:
    """Returns the n'th Central binomial coefficient as passed
        by the user. Function requires: import math or
        from math import factorial. In the latter case remove
        the "math." portion of math.factorial in the equations.

    parameters:
        n [int]: The user passed n'th coefficent request.

    returns:
        [int]: The Central binomial coefficient of the passed number (n).

    alternate definitions:
        def central_bin_coeff(n):              # try/except block reccommended.
        def central_bin_coeff(n) -> int:       # try/except block reccommended.
        def central_bin_coeff(n: int):         # try/except block not needed.
        def central_bin_coeff(n: int) -> int:  # try/except block not needed.
    """
    # Use the below return statement if the try/except block is not needed.
    # return math.factorial(2 * n) // (math.factorial(n)) ** 2

    # Use try/except block if lite error checking is needed.
    try:
        nth_coefficient = math.factorial(2 * n) // (math.factorial(n)) ** 2
    except ValueError as ve:
        print(f"ERROR: {ve}. Passed value must be an integer")
    except TypeError as te:
        print(f"ERROR: {te}. Passed value must be an integer")
    else:
        return nth_coefficient
    finally:
        pass


def main():
    # The 0th through 20th Central binomial coefficients example.
    for i in range(21):
        cbc: int = central_bin_coeff(i)
        print(f"{i}'th coefficient = {cbc}")

    # try/except lite error checking example.
    foo = central_bin_coeff("butter")
    foo = central_bin_coeff(3.14159)
    foo = central_bin_coeff(5)
    print(foo)


if __name__ == "__main__":
    main()

