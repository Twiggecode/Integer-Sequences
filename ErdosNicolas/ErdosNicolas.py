# Erdos Nicolas Numbers
import math

def find_divisors(n):
    divisors = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if i == n/i:
                divisors.append(i)
            else:
                divisors.extend([i, int(n//i)])
        i += 1
    divisors.sort()
    return divisors

def erdos_nicolas(num):
    divisors = find_divisors(num)
    for i in range(0, len(divisors)-2):
        if sum(divisors[0:i+1]) == num:
            return True
    return False

def main():
    n = int(input('Enter n: '))
    count = -1
    current = 0
    while count < n:
        current += 1
        if erdos_nicolas(current):
            count += 1
    print(current)

if __name__ == '__main__':
    main()
            

