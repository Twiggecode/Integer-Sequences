#!/usr/bin/env python3


def pow_two() -> int:
    return lambda m: 2 ** m


def main():
    foo = pow_two()
    print(foo(2))
    print(foo(8))
    print(foo(16))
    print(foo(64))


if __name__ == '__main__':
    main()
