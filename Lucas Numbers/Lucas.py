import math as Math
# this code returns the nth element of the Lucas numbers where n is a positive integer (or zero) input by the user

n = int()
while (True):
    n = int(input("Enter a number: "))
    if (n > -1):
        break
    print("Invalid number, please enter a new number.")

if (n==0):	# L0 is equal to 2
	print(2)

elif (n==1):	# L1 is equal to 1
    print(1)
    
elif (n==2):    # L2 is equal to 3
    print(3)

else:	# else n is greater than 2, and we use Ln = phi^n -(phi)^-n	where phi is the golden ratio
	print(round(Math.pow((1+Math.sqrt(5))/2,n) - Math.pow((-1+Math.sqrt(5))/2,n)))
