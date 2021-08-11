import math
def divisorSum(n):
        sum = 0
        j = 1
        while(j <= math.sqrt(n)):
                if(n % j == 0):
                        if(n / j == j):
                                sum = sum + j
                        else:
                                sum = sum + j
                                sum = sum + (n/j)
                j += 1
        return sum
        

def isDeficient(n):
        if(divisorSum(n) < (2 * n)):
                ans.append(n)
                return True
        return False

n = int(input("Enter the nth value to find : "))
count = 0
ans = []
i = 0
while(n >= count):
        if(isDeficient(i)):
                count += 1
        i += 1
print(ans)
        
        
