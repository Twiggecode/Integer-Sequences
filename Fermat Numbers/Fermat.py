# Iterative Function to calculate (x^y) in O(log y)
def power(x, y):
    res = 1  # Initialize result

    while (y > 0):

        # If y is odd,
        # multiply x with the result
        if (y & 1):
            res = res * x

        # n must be even now
        y = y >> 1  # y = y/2
        x = x * x  # Change x to x^2
    return res


# Function to find nth fermat number
def Fermat(i):
    # 2 to the power i
    power2_i = power(2, i)

    # 2 to the power 2^i
    power2_2_i = power(2, power2_i)

    return power2_2_i + 1


# Function to find first n Fermat numbers
def Fermat_Number(n):
    for i in range(n):

        # Calculate 2^2^i
        print(Fermat(i), end="")

        if (i != n - 1):
            print(end=", ")


if __name__ == '__main__':
    n = int(input("Enter the nth value to find : "))

    # Function call
    Fermat_Number(n)
