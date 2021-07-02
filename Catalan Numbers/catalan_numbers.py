""" Catalan Numbers (sequence A000108 in the OEIS) """
""" (2n)! / ((n + 1)!n!) """
# The first ten  (starting with n=0 are: 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862)

import math


def Catalan_Numbers(n):
    formula = math.factorial(2*n) / (math.factorial(n + 1) * math.factorial(n))
    return('C{} = {}'.format(n, formula))



print(Catalan_Numbers(n = int(input('Enter a Number: '))))
