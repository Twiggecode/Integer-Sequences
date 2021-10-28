import math

def get_sum(n: int) -> int:
    sum = 0
    i = 1

    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                sum += i
            else:
                sum += i
                sum = sum + (n / i)
        i += 1
    sum = sum - n
    return sum

def is_abundant(n: int) -> bool:
    if get_sum(n) > n:
        return True
    return False

def find_nth_value() -> None:
    n = int(input("Enter the nth value to find: "))
    count = 0
    i = 12

    while n >= count:
        if is_abundant(i):
            count += 1
        i += 1

    print(f"The value of Abundant Number is {i-1}")

if __name__ == "__main__":
    find_nth_value()
