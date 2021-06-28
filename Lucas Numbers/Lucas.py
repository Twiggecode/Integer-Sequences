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
		
else:	# else n is greater than 1, and we use Ln = (Ln-1) + (Ln-2)
	print(round(Math.pow((1+Math.sqrt(5))/2,n) - Math.pow((-1+Math.sqrt(5))/2,n)))
	