import math

def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True
    
def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 0
    while count < n:
        curr += 1
        if not isPrime(curr):
            count += 1
    print(curr)

main()
