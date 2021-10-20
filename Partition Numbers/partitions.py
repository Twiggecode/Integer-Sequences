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
    for item in res:
        item.sort()
    res_ = []
    [res_.append(x) for x in res if x not in res_]
    return res_

n = int(input('Enter n: '))
if n == 0:
    print(1)
else:
    print(len(partitions(n)))
    
