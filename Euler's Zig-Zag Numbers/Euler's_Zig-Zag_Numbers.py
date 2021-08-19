######################################
###     Euler ZigZag Numbers       ###
######################################

#Example : 1 1 1 2 5 16 61 272 1385 7936 50521 353792 2702765 22368256 .... 


def ZigZag(n):
        fact = [0 for i in range(n+1)]
        zig = [0 for i in range(n+1)]
        fact[0] = 1
        for i in range(1, n+1):
                fact[i] = fact[i-1]*i

        zig[0],zig[1] = 1,1
        
        for i in range(2,n):
                sum = 0
                for k in range(0, i):
                        sum += ((fact[i-1] // (fact[i-1-k] * fact[k])) * zig[k] * zig[i-1-k])
                zig[i] = sum//2
        return zig[n-1]
                

n = int(input("Enter the nth value to find : "))
print(n,"th value in Euler's Zig-Zag Numbers is ",ZigZag(n))
