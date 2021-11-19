import math

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
    
def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 2
    while count < n:
        curr += 1
        if not isPrime(curr):
            count += 1
    print(curr)

main()
