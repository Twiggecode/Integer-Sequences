def nats(n):
    i = n
    while True:
        yield i 
        i += 1

def sieve(s):
    n = next(s)
    yield n 
    yield from sieve(i for i in s if i%n != 0)

def primoral(n):
    res = 1
    i = 1
    primes = sieve(nats(2))
    while i <= n:
        res *= next(primes)
        i += 1
    return res

n = int(input('Enter n: '))
print(primoral(n))
    
