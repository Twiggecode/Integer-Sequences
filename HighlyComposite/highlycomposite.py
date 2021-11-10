import math

def findDivisors(n) :
    num_divisors = 0
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            num_divisors += 2 - (i == n/i)
        i += 1
    return num_divisors

def highlyComposite(num):
    n = findDivisors(num)
    for i in range(2, num, 2):
        if n <= findDivisors(i):
            return False
    return True

def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 0
    while count < n:
        curr += 1
        if highlyComposite(curr):
            count += 1
    print(curr)

main()
        
