#!/usr/bin/env python3


def pow_two() -> int:
    return lambda n: 2 ** n


def pow_series(end: int) -> None:
    series = pow_two()
    for i in range(0, end):
        print(series(i))


def main():
    stop = 10
    pow_series(stop)

    my_power_of_two = pow_two()
    result = my_power_of_two(16)
    print(result)

    foo = pow_two()
    result = foo(16)
    print()
    print(result)
    result /= 2
    result -= 1
    print(int(result))


if __name__ == '__main__':
    main()
