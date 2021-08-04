""" Catalan Numbers (sequence A000108 in the OEIS) """
""" (2n)! / ((n + 1)!n!) """
# The first ten  (starting with n=0 are: 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862)


def Catalan_Formula(n):
    formula = Fact(2 * n) / (Fact(n + 1) * Fact(n))
    return "C{} = {}".format(n, formula)


def Fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


print(Catalan_Formula(n=int(input("Enter a Number: "))))
