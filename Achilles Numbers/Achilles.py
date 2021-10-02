import math

def powerful(n):
    m = int(math.sqrt(n))
    for i in range(m+1):
        for j in range(i, m+1):
            if i**2 * j**3 == n or i**3 * j**2 == n:
                return True
    return False

def perfect_power(n):
    m = int(math.sqrt(n))
    for i in range(m+1):
        for j in range(n):
            if i**j == n:
                return True
    return False
            
def achilles(n):
    return powerful(n) and not perfect_power(n)

n = int(input('Enter n: '))
count = -1
current = 0
while count < n:
    current += 1
    if achilles(current):
        count += 1
print(current)
     
