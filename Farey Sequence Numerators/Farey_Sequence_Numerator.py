#This is one of the solution, I will come up with more optimal solution soon

def farey_sequence(n):
    l=[]
    for i in range(1,n+1):
        (a, b, c, d) = (0, 1, 1, i) #here a/b is first term and c/d is consecutive term
        l.append(0) #first farey seq. numerator will always be 0

        #following is the logic of next term in farey seq
        while (c <= i):
            k = (i + b) // d
            (a, b, c, d) = (c, d, k * c - a, k * d - b)
            l.append(a) #appending only the numerator, here its a
    return l[:n]
       

  
#taking input from user
n = int(input("Enter number of terms:"))

#printing numbers in comma separated manner
print(*farey_sequence(n), sep=",")





