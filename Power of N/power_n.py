import math

# Taking user input
def power_input():
    try:
        n = int(input("Enter n(power): "))
        return n
    except ValueError:  # This is needed to give line 13 an exception (Because it changes 'n')
        return power_input()

def base_input():
    try:
        m = int(input("Enter m(base): "))
        return m
    except ValueError:  # This is needed to give line 13 an exception (Because it changes 'n')
        return base_input()


# Find required number in a power series
def find_power_ofm():  # Power of 2 from wikipedia, means the n variable fills in the exponent
    n = power_input()
    m= base_input()
    while (
        True
    ):  # This loop is here just to prevent an error in case user inputs a negative number
        if n > -1:
            break
        else:
            print("Invalid input, please enter a positive number or 0.")
            n = power_input()

    number = math.pow(m, n)  # puts 2 to the power of n with function .pow
    return int(number)


# Main program
if __name__ == "__main__":
    print(f"The nth term in the sequence is {find_power_ofm()}")
