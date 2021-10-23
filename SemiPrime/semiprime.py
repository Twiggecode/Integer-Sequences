import math

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def isSemiprime(n):
    i = 2
    while i <= math.sqrt(n):
        if isPrime(i):
            if n % i == 0:
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
