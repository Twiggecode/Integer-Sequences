from math import gcd

def partitions(inp):
    res = []
    possible = [i for i in range(1, inp+1)]
    for num in possible:
        leftover = inp - num
        if leftover == 0:
            res.append([num])
        else:
            tails = partitions(leftover)
            for tail in tails:
                res.append([num] + tail)
    # sort the partitions
    for item in res:
        item.sort()
    res_ = []
    # Remove duplicates
    [res_.append(x) for x in res if x not in res_]
    return res_

def find_lcm(arr):
    lcm = 1
    for num in arr:
        lcm = lcm * num // gcd(lcm, num)
    return lcm

def Landau(n):
    parts = partitions(n)
    greatest = 1
    for partition  in parts:
        lcm = find_lcm(partition)
        if lcm > greatest:
            greatest = lcm
    return greatest
            
n = int(input('Enter n: '))
print(Landau(n))
