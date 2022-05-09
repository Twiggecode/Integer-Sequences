#!/usr/bin/python

'''
This algorithm determines if a number n is happy number.
'''


# This algorithm determines if a number is happy number.
def isHappy(n: int) -> bool:
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    while n != 1 and n != 4:
        n = get_next(n)

    return n == 1

# This algorithm returns the Nth happy number.
def happy(n: int) -> int:
    count, index = 0, 1
    while count <= n:
        if isHappy(index):
            count += 1
        index += 1

    return index - 1


def test(happy):
    assert happy(0) == 1
    assert happy(1) == 7
    assert happy(2) == 10
    assert happy(3) == 13
    assert happy(4) == 19
    assert happy(5) == 23
    assert happy(6) == 28
    assert happy(7) == 31
    assert happy(8) == 32


if __name__ == "__main__":
    test(happy)
