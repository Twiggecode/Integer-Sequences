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

def isCoprime(a, b):
    return math.gcd(a, b) == 1

def isCarmichael(n):
    if isPrime(n):
        return False
    if n % 2 == 0:
        for i in range(1, n, 2):
            if isCoprime(n, i):
                if i**(n-1) % n == 1:
                    continue
                else:
                    return False
    else:
        for i in range(1, n):
            if isCoprime(n, i):
                if i**(n-1) % n == 1:
                    continue
                else:
                    return False
    return True

def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 3
    while count < n:
        curr += 2
        if isCarmichael(curr):
            count += 1
    print(curr)

if __name__ == '__main__':
    main()

