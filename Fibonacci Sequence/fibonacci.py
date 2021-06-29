# This code will return the nth element of the Fibonacci sequence


def fibonacci(n):
    i=1
    num1,num2=0,1
    while i<n-1:
        if n==1:
            return 0
        sum=num1+num2
        num1,num2=num2,sum
        i += 1
    return sum

my_num=int(input("Enter a number:"))
print(f"The {my_num}th element of fibonacci series is:",fibonacci(my_num))