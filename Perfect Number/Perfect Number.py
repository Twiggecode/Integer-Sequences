def isPerfect( n ):
     
    # To store sum of divisors
    sum = 1
     
    # Find all divisors and add them
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1
     
    # If sum of divisors is equal to
    # n, then n is a perfect number
     
    return (True if sum == n and n!=1 else False)
 
# Driver program
# to print the first N perfect numbers
n=int(input())
for i in range (n):
    if isPerfect (i):
        print(i,end=" ")
        
        
