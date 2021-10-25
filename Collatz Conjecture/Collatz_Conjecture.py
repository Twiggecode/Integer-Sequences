# Python3 program to implement Collatz Conjecture
# Function to find if n reaches to 1 or not.

# O(n) solution

def isToOneRec(n: int, s: set) -> bool:
    if n == 1:
        return True
  
    # If there is a cycle formed,
    # we can't reach 1.
    if n in s:
        return False
  
    # If n is odd then pass n = 3n+1 else n = n/2
    if n % 2:
        return isToOneRec(3 * n + 1, s)
    else:
        return isToOneRec(n // 2, s)
  
# Wrapper over isToOneRec()
def isToOne(n: int) -> bool:
  
    # To store numbers visited
    # using recursive calls.
    s = set()
  
    return isToOneRec(n, s)
  
# Driver Code
if __name__ == "__main__":
    n = int(input())
    if isToOne(n):
        print("Yes, the number reaches to one after the above operations  ")
    else:
        print("No, it does not reach one ")
        
# We can also make use of the Collatz conjecture which states that every positive number 
#can reach to one after the following operations (in the commnets above)

# O(1) solution

# Uncomment below code to see the O(1) solution

#def isToOne(n):
  
#     # Return true if n
#     # is positive
#     return (n > 0)
  
# # Drivers code
# n = int(input())
  
# if isToOne(n) == True:
#     print("Yes")
# else:
#     print("No")
