import math
from itertools import combinations

def find_divisors(n):
    divisors = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if i == n/i:
                divisors.append(i)
            else:
                divisors.extend([i,int(n/i)])
        i += 1
    divisors.remove(n)
    divisors.sort()
    return divisors

def subset_generator(arr):
    for i in range(1, len(arr) + 1):
        for elem in combinations(arr, i):
            yield elem

def isWeird(num):
    isSemiPerfect = False
    isAbundant = False
    divisors = find_divisors(num)
    if sum(divisors) > num:
        isAbundant = True
    for subset in subset_generator(divisors):
        if sum(subset) == num:
            isSemiPerfect = True
    return isAbundant and not isSemiPerfect

def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 0
    while count < n:
        curr += 1
        if isWeird(curr):
            count += 1
    print(curr)

main()









