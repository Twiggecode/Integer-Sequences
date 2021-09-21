#!/usr/bin/env python3


def pow_two(n: int) -> int:
    return lambda n: n ** 2


def main():
    foo = pow_two(2)
    for i in range(5):
        print(foo(i))


if __name__ == '__main__':
    main()
