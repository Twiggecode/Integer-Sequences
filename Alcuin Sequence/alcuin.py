from itertools import combinations_with_replacement
import math

def alcuin(n):
    count = 0
    r = math.ceil(n/2)
    possible = [combination for combination in combinations_with_replacement([i for i in range(1, r+1)], 3)]
    possible = filter(lambda x : x[0] + x[1] + x[2] == n and 2*max(x) < (x[0]+x[1]+x[2]), possible)
    print(len(list(possible)))
                       
n = int(input('Enter n: '))
alcuin(n)
