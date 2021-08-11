def cullen_number(n):
    return n * (2 ** n) + 1


if __name__ == "__main__":

    while True:
        number = int(input("Enter a number: "))

        if number > -1:
            break

        else:
            print("Natural number expected!")

    print(cullen_number(number))
