import math 
from itertools import permutations

def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def isPermutablePrime(num):
    for p in permutations(str(num)):
        test = ''.join(p)
        if not isPrime(int(test)):
            return False
    return True
        
def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 1
    while count < n:
        curr += 1
        if isPermutablePrime(curr):
            count += 1
    print(curr)

main()
