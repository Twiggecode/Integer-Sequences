import math
from itertools import permutations

def alternating(arr):
    breakpoint()
    i = 0
    flag = 0
    while i < len(arr) - 1:
        if flag:
            if arr[i+1] > arr[i]:
                flag = not flag
            else:
                return False
        else:
            if arr[i+1] < arr[i]:
                flag = not flag
            else:
                return False
        i += 1
    return True

def downup_permutations(n):
    p = list(permutations([i for i in range(1, n+1)], n))
    downup = filter(alternating, p)
    return list(downup)

def euler(n):
    return len(downup_permutations(2*n))

n = int(input('Enter n: '))
print(euler(n))
