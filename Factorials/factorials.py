def factorial(a:int):
    if a == 0 or a == 1:
        return 1

    if a<0:
        return "Negative Integer is not allowed"

    output = a * factorial(a-1)
    return output








if __name__ == "__main__":
    n = int(input("Enter the positive integer value: "))
    answer = factorial(n)
    print(f"{n}! = {answer}")
    

