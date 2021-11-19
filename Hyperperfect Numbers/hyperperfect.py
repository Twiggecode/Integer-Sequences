import math

def divisor_function(num):
    i = 1
    s = 0
    while i * i <= num:
        if num % i == 0:
            if i == num/i:
                s += i
            else:
                s += i + num/i
        i += 1
    return int(s - num)

def isHyperPerfect(num):
    d = divisor_function(num)
    if d - 1 == 0:
        return False
    if (num - 1) % (d - 1) == 0:
        return True
    else:
        return False
    
def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 5
    while count < n:
        curr += 1
        if isHyperPerfect(curr):
            count += 1
    print(curr)

main()
