#importing required libraries
import math

#function to find Sn 
def Sn(n):
    return math.floor(1 + math.log2(n))

#take input
n = int(input("Enter number of elements you want of sorting number:"))

#print sequence of n sorting numbers
for i in range(1,n+1):
    x = i*Sn(i) - pow(2,Sn(i)) + 1 #this is formula for sorting numbers
    print(x,end=" ")
