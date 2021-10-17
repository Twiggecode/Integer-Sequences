# Script to find the n-th Achilles Number in sequence
# Achilles Numbers are defined as a Powerful number, but not a Perfect Power
# Powerful numbers can be defined as all prime factors of the number (p) also have p^2 as a factor.
# As prime factors will already be found, determining a Perfect Power is as simple
# as determining if the GCD of all powers = 1.

# math is used to calculate GCD of the list of prime factors
import math
# functools is used to apply the math.gcd function to a list of factors (as opposed to just two factors)
# As of Python 3.9, could just use the math.gcd() function as it allows a list input now.
import functools


# Function to return a list of prime factors
def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        # loop through each integer up to the square root of n
        if n % i == 0:
            # if it is a factor, add it to the list for returning later
            factors.append(i)
            # reduce the remaining number by the factor appended
            n //= i
        else:
            # otherwise, try the next integer
            i += 1

    if n > 1:
        # then there is a remaining factor
        factors.append(n)

    return factors


# Function to return a list of the factor powers based on a list of prime factors passed
def factor_powers(factors):
    powers = []
    # Use prior_factor to compare if it's the same as the previous factor
    prior_factor = factors[0]
    i = 0
    for a in factors:
        # If the next item in the list is the same factor, increase the count
        if a == prior_factor:
            i += 1
        # Otherwise, append the count that's there, reset the count to 1 and start matching to the new factor
        else:
            powers.append(i)
            i = 1
            prior_factor = a
    # Have to append a count of the last factor
    powers.append(i)
    return powers


def is_powerful(powers):
    if min(powers) >= 2:
        return True
    else:
        return False


def is_perfect_power(powers):
    if len(powers) <= 1:
        return True
    elif len(powers) == 2:
        return math.gcd(powers[0], powers[1]) != 1
    elif len(powers) >= 3:
        return functools.reduce(math.gcd, powers) != 1
    else:
        return False


def is_achilles(n):
    # First retrieve the powers of all prime factors
    powers = factor_powers(get_prime_factors(n))
    # Then return if it is powerful, but no a perfect power
    return is_powerful(powers) and not is_perfect_power(powers)


# Main program to prompt for the sequence number and loop to find that n in the sequence

num = int(input('Enter n: '))
count = 0
current = 2
while count < num:
    current += 1
    if is_achilles(current):
        count += 1
print(current)
