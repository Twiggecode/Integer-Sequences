# Similar to Fibonacci sequence with similar recursive structure
# Function returns nth element of Padovan sequence
# P(n) = P(n-2) + P(n-3)
# P(0) = P(1) = P(2) = 1
# 0th ,1st and 2nd number of the series are 1
# Find nth Padovan number using iterative formula for better linear complexity


def padovan(n):

    pPrevPrev, pPrev, pCurr, pNext = 1, 1, 1, 1

    for i in range(3, n):
        pNext = pPrevPrev + pPrev
        pPrevPrev = pPrev
        pPrev = pCurr
        pCurr = pNext

    return pNext


def main():

    while True:
        n = int(input("Enter a number: "))
        if n >= 0:
            break

        print("Invalid number,try again")

    print(f"P({n}) = {padovan(n)}")


main()
