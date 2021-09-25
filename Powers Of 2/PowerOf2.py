import math

# Taking user input
def user_input():
    try:
        n = int(input("Enter n: "))
        return n
    except ValueError:  # This is needed to give line 13 an exception (Because it changes 'n')
        return user_input()


# Find required number in a power series
def find_power_of2():  # Power of 2 from wikipedia, means the n variable fills in the exponent
    n = user_input()

    while (
        True
    ):  # This loop is here just to prevent an error in case user inputs a negative number
        if n > -1:
            break
        else:
            print("Invalid input, please enter a positive number or 0.")
            n = user_input()

    number = math.pow(2, n)  # puts 2 to the power of n with function .pow
    return int(number)


# Main program
if __name__ == "__main__":
    print(f"The nth term in the sequence is {find_power_of2()}")
