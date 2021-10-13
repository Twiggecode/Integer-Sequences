# Python3 program to check if a number
# is Stella octangula number
 
# Returns value of n*(2*n*n - 1)
def f(n):
     
    return n * (2 * n * n - 1);
 
# Finds if a value of f(n) is equal to x
# where n is in interval [low..high]
def binarySearch(low, high, x):
 
    while (low <= high):
        mid = int((low + high) // 2);
 
        if (f(mid) < x):
            low = mid + 1;
        elif (f(mid) > x):
            high = mid - 1;
        else:
            return True;
             
    return False;
 
# Returns true if x isStella octangula
#  number. Else returns false.
def isStellaOctangula(x):
 
    if (x == 0):
        return True;
 
    # Find 'high' for binary search
    # by repeated doubling
    i = 1;
    while (f(i) < x):
        i = i * 2;
 
    # If condition is satisfied for a
    # power of 2.
    if (f(i) == x):
        return True;
 
    # Call binary search
    return binarySearch(i / 2, i, x);
 
# Driver code
n=int(input())
for i in range(n):
    if (isStellaOctangula(i) == True):
        print(i,end=" ");
