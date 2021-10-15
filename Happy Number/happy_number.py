#!/usr/bin/python

'''
This algorithm determines if a number n is happy number.
'''

def main():
    n = int(input("Enter a number : "))

    def recursion(n):
        rem = 0
        total = 0
        # Loop to square each digit and then add them
        while (n != 0):
            rem = n % 10
            n = n // 10
            total += rem**2
        return total

    while True:
        if(recursion(n) == 1):
            print("True")
            return True
        n = recursion(n)
        if (n < 10):
            print("False")
            return False

if __name__ == "__main__":
    main()
