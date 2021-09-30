def find_divisors(n):
    divisors = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def isPerfect(n):
    divisors = find_divisors(n)
    sum_divisors = sum(divisors)
    if sum_divisors == n:
        return True, divisors
    else:
        return False, divisors

def isErdosNicols(n):
    perfect, divisors = isPerfect(n)
    if perfect:
        return False
    for i in range(1, len(divisors)):
        if sum(divisors[0:i+1]) == n:
            return True
    return False

n = int(input('Enter n: '))
count = -1
current = 0
while count < n:
    current += 1
    if isErdosNicols(current):
        count += 1
print(current)

