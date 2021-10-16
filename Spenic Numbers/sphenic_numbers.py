import math

def primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            for j in range(2*i, n, i):
                sieve[j] = False
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def isSpehnic(num):
    p = primes(num)
    # The very smallest combiantion of primes would contain 2 and 3
    # We only need to check numbers <= num/6
    p = [n for n in p if n <= num//6]
    l = len(p)
    for i in range(l - 2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if p[i] * p[j] * p[k] == num:
                    return True
    return False

def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 0
    while count < n:
        curr += 1
        if isSpehnic(curr):
            count += 1
    print(curr)

main()
