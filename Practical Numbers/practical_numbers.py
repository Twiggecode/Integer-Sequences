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
                divisors.extend([i, int(n/i)])
        i += 1
    divisors.sort()
    divisors.pop()
    return divisors

def check(num, arr):
    combs = [elem for i in range(1, len(arr)+1) for elem in combinations(arr, i)]
    return any([sum(c)==num for c in combs])

def is_practical(num):
    divs = find_divisors(num)
    for n in range(2, num):
        if not check(n, divs):
            return False
    return True
   
def main():
    n = int(input('Enter n: '))
    count = -1
    current = 0
    
    # From https://en.wikipedia.org/wiki/Practical_number:
    # "The only odd practical number is 1, because if n is an odd number greater than 2, 
    # then 2 cannot be expressed as the sum of distinct divisors of n."
    # Thus we don't need to check the odd numbers greater than 2, and this can improve the time complexity. 
    
    # To check for 0,1 and 2
    while current < 2 and count < n:
        current +=1
        if is_practical(current):
            count += 1
    
    # To check for greater numbers, only check even numbers
    while count < n:
        current += 2
        if is_practical(current):
            count += 1
    print(current)

if __name__ == '__main__':
    main()
