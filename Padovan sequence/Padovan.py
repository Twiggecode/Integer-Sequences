# Function returns nth element of Padovan sequence
def padovan(n):

    p = 0
    if n > 2:
        p = padovan(n - 2) + padovan(n - 3)
        return p

    else:
        p = 1
        return p


def main():

    while True:
        n = int(input("Enter a number: "))
        if n >= 0:
            break

        print("Invalid number,try again")

    print(f"P({n}) = {padovan(n)}")


main()
