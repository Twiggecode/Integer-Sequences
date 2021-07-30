def factorial(a: int):
    """
    handle edge case
    a == 0 or 1 or -ve number
    """
    if a == 0 or a == 1:
        return 1

    if a < 0:
        return "Negative Integer is not allowed"

    # recursive call
    return a * factorial(a - 1)


if __name__ == "__main__":
    n = int(input("Enter the positive integer value: "))
    answer = factorial(n)
    print(f"{n}! = {answer}")
