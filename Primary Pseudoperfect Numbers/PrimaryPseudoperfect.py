import math

thresh = 0.0000001

def primeFactors(n):
    divisors = set()
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        divisors.add(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        # while i divides n , print i and divide n
        while n % i== 0:
            divisors.add(i)
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        divisors.add(n)
    return divisors

def isPrimaryPseudoperfect(num):
    prime_factors = primeFactors(num)
    s = 0 
    for p in prime_factors:
        s += 1/p
    return abs(((1/num) + s) - 1) <= thresh

def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 1
    while count < n:
        curr += 1
        if isPrimaryPseudoperfect(curr):
            count += 1
    print(curr)

main()
