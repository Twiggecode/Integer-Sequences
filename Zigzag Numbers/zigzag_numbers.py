from itertools import permutations

def check_if_alternating(arr):
    if len(arr) <= 1:
        return True
    for i in range(len(arr)-1):
        if i % 2 == 0:
            if arr[i+1] > arr[i]:
                continue
            else:
                return False
        else:
            if arr[i+1] < arr[i]:
                continue
            else:
                return False
    return True

def zigzag(n):
    print(len(list(filter(check_if_alternating, list(permutations([i for i in range(1,n+1)]))))))

n = int(input('Enter n: '))
zigzag(n)
    
