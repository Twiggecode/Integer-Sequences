#!/usr/bin/env python3
"""Python script to save a series of numbers, print the
series of numbers provided the numbers are deficient
"""


def print_deficients(begin: int, end: int) -> None:
    def_list: list[int] = []
    sum_divisors: int = 0
    index: int = 1

    while True:
        for i in range(begin):
            if i == 0:
                continue
            elif begin % i:
                sum_divisors += 1

        if sum_divisors < 2 * begin:
            def_list.append(begin)

        if begin == end:
            break

        begin += 1

    return def_list



def main():
    # start = int(input("Enter start number: "))
    # stop = int(input("Enter stop number: "))
    start, stop = 1, 20
    deficients = print_deficients(start, stop)
    [print(number) for number in deficients]


if __name__ == '__main__':
    main()

