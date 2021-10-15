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
    
    a = 0
    b = 1
    c = 1
    
    for i in range(3, n + 1):
        temp = a + b + c
        a, b, c = b, c, temp
        
    print(temp)


if __name__ == "__main__":
    main()
