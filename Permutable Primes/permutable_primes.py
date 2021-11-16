import math 
from itertools import permutations

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
