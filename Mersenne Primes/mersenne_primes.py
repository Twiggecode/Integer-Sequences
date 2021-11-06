import math

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

def powers_of_two():
    p = 1
    while True:
        p = 2 * p
        yield p

def main():
    n = int(input('Enter n: '))
    count = -1
    g = powers_of_two()
    while count < n:
        curr = next(g)
        if isPrime(curr - 1):
            count += 1
    print(curr - 1)

if __name__ == '__main__':
    main()
    
    
