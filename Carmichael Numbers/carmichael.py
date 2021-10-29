import math

def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True
    
def isCarmichael(n):
    if isPrime(n):
        return False
    for i in range(1, n):
        if i**n  % n == i:
            continue
        else:
            return False
    return True

def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 0
    while count < n:
        curr += 1
        if isCarmichael(curr):
            count += 1
    print(curr)

main()
