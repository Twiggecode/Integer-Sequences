import math

def isPrime(num):
    if num <= 3:
        return num > 1
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False
    i = 5
    while i <= math.sqrt(num):
        if num % (i) == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True

def nats(n):
    i = n
    while True:
        yield i 
        i += 1

def sieve(s):
    n = next(s)
    yield n 
    yield from sieve(i for i in s if i%n != 0)

def primorial(n):
    res = 1
    i = 1
    primes = sieve(nats(2))
    res *= next(primes)
    while i <= n:
        res *= next(primes)
        i += 1
    return res

def fortunate(n):
    p = primorial(n)
    m = 2
    while not isPrime(p+m):
        m += 1
    return m

n = int(input('Enter n: '))
print(fortunate(n))
    
