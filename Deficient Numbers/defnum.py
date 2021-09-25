#!/usr/bin/env python3
"""Python script to save a series of numbers, print the
series of numbers provided the numbers are deficient
"""


def print_deficients(begin: int, end: int) -> None:
    if type(begin) != int or type(end) != int:
        raise ValueError("\nThe begin and the end number must be integers\n")

    deficient_nums = []

    while begin <= end:
        divisors: int = begin

        index: int = 1
        while index <= begin // 2:
            if begin % index == 0:
                divisors += index
            index += 1

        if divisors < (2 * begin):
            deficient_nums.append(begin)
            # print(f"{begin} is deficient")

        begin += 1

    return deficient_nums

def main():
    # start = int(input("Enter start number: "))
    # stop = int(input("Enter stop number: "))
    start, stop = 10, 20
    deficients = print_deficients(start, stop)
    print()
    [print(number) for number in deficients]


if __name__ == '__main__':
    main()

