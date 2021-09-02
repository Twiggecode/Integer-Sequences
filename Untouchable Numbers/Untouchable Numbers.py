import math
 
def divSum(num):
 
    result = 0
 
    for i in range(2, int(math.sqrt(num))):
        if (num % i == 0):
            if (i == (num // i)):
                result += i
            else:
                result += (i + num // i)
    return (result + 1)
 
def isUntouchable(n):
 
    for i in range(1, 2 * n):
        if (divSum(i) == n):
            return False
    return True
 
N = int(input("Enter the nth value to find : "))
if (isUntouchable(N)):
    print("Yes")
else:
    print("No")
