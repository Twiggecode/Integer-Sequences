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

def isSemiprime(n):
    i = 2
    while i <= math.sqrt(n):
            if n % i == 0:
                if isPrime(i):
                    if isPrime(n/i):
                        return True
        i += 1
    return False
    
def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 0
    while count < n:
        curr += 1
        if isSemiprime(curr):
            count += 1
    print(curr)

main()
