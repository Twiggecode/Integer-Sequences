# Function to return the Nth number of the modified Fibonacci series where A and B are the first two terms
def findNthNumber(a, b, n):
 
    # To store the current element which is the sum of previous two elements of the series
    sum = 0
 
    # This loop will terminate when the Nth element is found
    for i in range(2, n):
        sum = a + b
        a = b
        b = sum
     
    # Return the Nth element
    return sum
 
# Driver code
if __name__ == '__main__':
    a = 5
    b = 7
    n = 10
 
    print(findNthNumber(a, b, n))
 

 #the output is 343
# you can test it by using any number of your choice