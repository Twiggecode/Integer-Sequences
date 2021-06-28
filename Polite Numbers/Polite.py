import math as Math

# this code returns the nth element of the Polite numbers where n is a positive integer input by the user
# the polite numbers are the sequence of natural numbers that are not powers of 2


i = 1
count = 0
n = int()

# the loop is used to check if the number input by the user is a positive integer
while (True):
    n = int(input("Enter a number: "))
    if (n > -1):
        break
    print("Invalid number, please enter a new number.")


while (count<=n): # count the first n natural numbers that are not powers of 2, which will return the nth polite number
    if((Math.log(i))/(Math.log(2)) != round((Math.log(i))/(Math.log(2)))): # check if a number is not power of 2
        count+=1	# count will not increment if the number is a power of 2
    i+=1

print(i-1)
