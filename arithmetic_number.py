import math

def main():
    """
    Ask for user's input and calls function to find arithmetic number
    """
    # Ask for user's input
    try:
        n = int(input("Please enter a non-negative integer: "))
    # Check for error of not inputting an integer
    except ValueError:
        print("Invalid input. Please try again.")
        return None
    else:
        # Check if user inputs a negative integer
        if n < 0:
            print("Input cannot be a negative integer. Please try again.")
            return None
    # Find nth arithmetic number
    print(arithmetic_number(n))


def arithmetic_number(n):
    """
    n (int): number
    Returns the nth arithmetic number
    """
    # Initialize the position of arithmetic number
    position = 0
    # Initialize the number at which one should check if arithmetic number
    number = 1

    while True:
        # Check if an arithmetic number
        if average_of_factors(number).is_integer():
            # Check if the arithmetic number is at position the user asked for
            if position == n:
                return number
            position += 1
        number += 1


def average_of_factors(n):
    """
    n (int): number
    Returns the average of the positive divisors of n
    """
    # Initialize the sum
    total = 0
    # Initialize the number of factors
    count = 0
    for i in range(1, n+1):
        # Check if i is a divisor of n
        if n % i == 0:
            total += i
            count += 1
    average = total/count
    return average


if __name__ == "__main__":
    main()
