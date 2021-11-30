import math

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
    divisors.sort()
    return divisors

def isSuperperfect(num):
    return sum(find_divisors(sum(find_divisors(num)))) == 2*num

def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 0
    while count < n:
        curr += 2
        if isSuperperfect(curr):
            count += 1
    print(curr)

main()
