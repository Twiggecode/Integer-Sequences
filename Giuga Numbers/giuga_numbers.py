import math 

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

def isPrime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i < n:
        if n % (i) == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def giuga(num):
    prime_factors = primeFactors(num)
    for p in prime_factors:
        if (num - p) % (p**2) != 0:
            return False
    return True
            

def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 2
    while count < n:
        curr += 1
        if not isPrime(curr):
            if giuga(curr):
                count += 1
    print(curr)

main()
