# Python3 implementation of the approach 
  
# Function to return the smallest prime factor of n 
def smallestPrimeFactor(n): 
  
    # Initialize i = 2 
    i = 2
  
    # While i <= sqrt(n) 
    while (i * i) <= n : 
  
        # If n is divisible by i 
        if n % i == 0: 
            return i 
  
        # Increment i 
        i += 1
    return n 
  
# Function to print the first n 
# terms of the required sequence 
def solve(n): 
  
    # To store the product of the previous terms 
    product = 1
  
    # Traverse the prime numbers 
    i = 0
    while i < n: 
  
        # Current term will be smallest prime 
        # factor of (1 + product of all previous terms)
        num = smallestPrimeFactor(product + 1) 
  
        # Print the current term 
        print(num, end=' ') 
  
        # Update the product 
        product = product * num 
        i += 1
  
# Driver code 
# Find the first 14 terms of the sequence 
b = int(input())
solve(b)
