#!/usr/bin/env python3
# TODO: Comment code


def pow_two() -> int:
    """[summary]

    Returns:
        int: [description]
    """
    return lambda n: 2 ** n


def pow_series(end: int) -> None:
    """[summary]

    Args:
        end (int): [description]
    """
    series = pow_two()
    for i in range(0, (end + 1)):
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
