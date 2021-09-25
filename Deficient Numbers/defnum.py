#!/usr/bin/env python3
"""Python script to save, as a list, a series of numbers that
are deficient. Numbers are deficient if sum(m) < 2 * m, whith sum(m) being
the summation of m's divisors. Scripts gives the option to print the list of
deficient nubmers.
"""


def print_deficients(begin: int, end: int) -> int:
    """print_deficients(begin, end) -> int:

    Calculates if a series of number between begin, and end, [inclusive] are
    deficient and appends the deficient number to a list

    parameters:
        begin: [int]: First number to calculate
        end: [int]: Last number to calculate
    returns:
        deficient_nums: list[int]: List of deficient numbers calculated
    """
    deficient_nums: list[int] = []

    while begin <= end:
        # We stop iterating half-way to begin and since begin is a divisor of
        # begin we set divisors variable to begin
        divisors: int = begin

        index: int = 1
        # Iterate to half of begin since numbers greater than (begin / 2) will
        # not be divisors
        while index <= begin // 2:
            if begin % index == 0:  # Checks if divisor
                divisors += index  # sums divisor if i is a divisor

            index += 1

        if divisors < 2 * begin:  # Checks for deficiency
            deficient_nums.append(begin)  # Appends to list if deficient

        begin += 1  # Increment one number closer to end variable

    return deficient_nums


def check_if_deficient():
    """check_fi_dificient():
    TODO: Future implimentation.
    """
    pass


def main() -> None:
    # Gets users start and stop value. Raises ValueError if number is not an int
    start = int(input("Enter start number: "))
    stop = int(input("Enter stop number: "))
    # start, stop = 940, 950

    deficients = print_deficients(start, stop)

    #  Query's user if they wish to print the returned list of dificient nubers
    if str(input("Enter 'y' to print the dificient numbers: ").lower()) == 'y':
        print()
        [print(f"{number} is deficient") for number in deficients]


if __name__ == '__main__':
    main()

