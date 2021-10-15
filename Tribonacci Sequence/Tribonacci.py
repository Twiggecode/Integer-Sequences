#!/usr/bin/python

# This code will return the nth element of the Tribonacci sequence

def main():

    n = int(input("Enter number:"))
        
    if(n == 0):
        print("0")
    if(n == 1):
        print("1")
    if(n == 2):
        print("1")
    
    # Assigning variables to first 3 elements of Tribonacci sequence
    a = 0
    b = 1
    c = 1
    
    # For loop for finding the nth number in sequence 
    for i in range(3, n + 1):
        n_number = a + b + c
        a, b, c = b, c, n_number
        
    print(n_number)


if __name__ == "__main__":
    main()
