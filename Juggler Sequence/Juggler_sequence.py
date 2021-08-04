import math

num: int
while True:
    try:
        num = int(input("Enter a number: "))
        if num > -1:
            break
    except:
        print("Enter a positive integer: ")

# This function prints the juggler Sequence
def printJuggler(n):
    a = n

    # print the first term
    print(a)

    # calculate terms until last term is not 1
    while a != 1:
        b = 0

        # Check if previous term is even or odd
        if a % 2 == 0:

            # calculate next term
            b = (int)(math.floor(math.sqrt(a)))

        else:
            # for odd previous term calculate
            # next term
            b = (int)(math.floor(math.sqrt(a) * math.sqrt(a) * math.sqrt(a)))

        print(b)
        a = b


print(f"The juggler sequence for {num} is : ")
printJuggler(num)
