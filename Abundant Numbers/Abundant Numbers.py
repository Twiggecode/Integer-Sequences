import math

def getSum(n):
        sum = 0
        i = 1
        while( i <= (math.sqrt(n))):
                if(n%i == 0):
                        if( n/i == i):
                                sum += i
                        else:
                                sum += i
                                sum = sum + (n / i)
                i += 1
        sum = sum - n
        return sum

def isAbundant(n):
        if(getSum(n) > n):
                return True
        return False

n = int(input("Enter the nth value to find : "))
count = 0
ans = []
i = 0
while(n >= count):
        if(isAbundant(i)):
                ans.append(i)
                count += 1
        i += 1
print(n,"th value of Abundant Number is ",ans[n])
        
