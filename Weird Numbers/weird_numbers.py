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
    return divisors

def subset_generator(arr):
    for i in range(1, len(arr) + 1):
        for elem in combinations(arr, i):
            yield elem

def isWeird(num):
    divisors = find_divisors(num)
    if not (sum(divisors) > num):
        return False
    for subset in subset_generator(divisors):
        if sum(subset) == num:
            return False
    return True

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



