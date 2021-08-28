'''
Explanation for Euler's Totient Function

Φ(1) = 1  
gcd(1, 1) is 1

Φ(2) = 1
gcd(1, 2) is 1, but gcd(2, 2) is 2.

Φ(3) = 2
gcd(1, 3) is 1 and gcd(2, 3) is 1

Φ(4) = 2
gcd(1, 4) is 1 and gcd(3, 4) is 1

Φ(5) = 4
gcd(1, 5) is 1, gcd(2, 5) is 1, 
gcd(3, 5) is 1 and gcd(4, 5) is 1

'''

def gcd(a, b):
        if(a == 0):
                return b
        return gcd(b%a, a)


def phi(n):
        res = 1
        for i in range(2,n):
                if(gcd(i, n) == 1):
                        res += 1
        return res

n = int(input("Enter the nth value to find : "))
print("Phi value for ",n,"is : ", phi(n))
