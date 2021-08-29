import math

def divsum(n):
        if n == 1:
                return 0
        res = 0
        i = 2
        while( i <= math.sqrt(n)):
                if(n%i == 0):
                        if(i == (n/i)):
                                res += i
                        else:
                                res += (i + n/i)
                i += 1
        return (int)(res+1)


n = int(input("Enter the nth value to find :"))
print(n,"th number sum of all divisors is : ",divsum(n))
