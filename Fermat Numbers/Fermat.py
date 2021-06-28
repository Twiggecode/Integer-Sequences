import math as Math
# this class returns the nth element of the Fermat numbers where n is a positive integer (or zero) input by the user

# the loop is used to check if the number input by the user is a positive integer or zero
n = int()
while (True):
    n = int(input("Enter a number: "))
    if (n > -1):
        break
    print("Invalid number, please enter a new number.")
    
print(round(Math.pow(2,Math.pow(2,n)) +1));		# calculate the Fermat numbers using Fn = 2^(2^n)  + 1			