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

def isSemiperfect(num):
    divisors = find_divisors(num)
    subsets = [elem for i in range(1, len(divisors) + 1) for elem in combinations(divisors, i)]
    for subset in subsets:
        if sum(subset) == num:
            return True
    return False
    
def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 0
    while count < n:
        curr += 1
        if isSemiperfect(curr):
            count += 1
    print(curr)

main()
