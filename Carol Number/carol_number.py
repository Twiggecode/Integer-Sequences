"""The first few Carol numbers are: −1, 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527 (sequence A093112 in the OEIS)."""


def Carol_Numbers():
    n = int(input("Enter a Number: "))
    formula = (((2 ** n) - 1) ** 2) - 2
    print(formula)


Carol_Numbers()
