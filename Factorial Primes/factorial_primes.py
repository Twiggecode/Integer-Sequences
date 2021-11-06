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

def factorial_generator():
    x = 1
    count = 1
    while True:
        x = x * count
        yield x
        count += 1

def main():
    n = int(input('Enter n: '))
    g = factorial_generator()
    count = -1 
    res = 0
    while count < n:
        curr = next(g)
        if isPrime(curr-1):
            count += 1
            if count == n:
                res = curr - 1
                break
        if isPrime(curr+1):
            count += 1
            if count == n:
                res = curr + 1
                break
    print(res)
    
if __name__ == '__main__':
    main()
    
    
    
        
        
        
    
