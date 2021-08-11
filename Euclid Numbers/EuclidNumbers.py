# Python 3 program to check
# Euclid Number
MAX = 10000

arr = []

# Function to generate prime numbers
def SieveOfEratosthenes():

    # Create a boolean array "prime[0....n]"
    # and initialize all entries it as
    # true. A value in prime[i] will
    # finally be false if i is Not a
    # prime, else true.

    # implementation works because prime nunbers have only
    # themselves as their factor. So if any number say 7 is
    # finally left as true in prime array then it means that
    # it is a prime.
    prime = [True] * MAX

    p = 2
    while p * p < MAX:

        # If prime[p] is not changed,
        # then it is a prime
        if prime[p] == True:

            # Update all multiples of p
            for i in range(p * 2, MAX, p):
                prime[i] = False

        p += 1

    # store all prime numbers
    # to vector 'arr'
    for p in range(2, MAX):
        if prime[p]:
            arr.append(p)


# Function to check the number
# for Euclid Number
def isEuclid(n):

    product = 1
    i = 0

    while product < n:

        # Multiply next prime number
        # and check if product + 1 = n
        # holds or not
        product = product * arr[i]

        if product + 1 == n:
            return True

        i += 1

    return False


# if the number is Euclid we print True
# otherwise we print False
if __name__ == "__main__":
    n = int(input())
    if isEuclid(n):
        print(True)
    else:
        print(False)
