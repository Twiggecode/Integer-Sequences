# Lazy caterer's sequence 

# describes the maximum number of pieces a circular pizza
# can be divided into with an increasing number of cuts,n.
# recursive formula is f(n) = f(n-1) + n

# EDIT:
# This leads to a time complexity of O(n)
# Optimising the formula
# f(n) = n+ f(n-1) = {n + (n-1) + f(n-2)...+1} + f(0) = {(n*(n+1))/2} +1
# This optimises time complexity to O(1)

n = int(input("Enter a number: "))
ans= str(int((n*(n+1))/2 +1))
print("A circular pizza can be divided into "+ans+" pieces with "+str(n)+" cuts!")
  
