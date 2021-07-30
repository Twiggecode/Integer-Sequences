""" Narayana's cows
Function to print nth term of the Narayana's cows sequence where n==0 returns the first number
The number of cows each year if each cow has one cow a year beginning its fourth year. 
 	{1, 1, 1, 2, 3, 4, 6, 9, 13, 19, ...} """

nth = input(
    "Please enter a positive integer to return its value in the Narayana's cows sequence:"
)

errormessage = "Invalid input, please enter a positive integer:"  # Displyed when invalid input is given

while True:
    try:
        int(nth)  # Checking whether the input string is a whole number
    except:
        nth = input(errormessage)
        continue
    if int(nth) < 0:  # Checking that input is not a negative number
        nth = input(errormessage)
        continue
    else:
        n = int(nth)  # Converting the input into an integer
        break


def Narayancows(n):
    if n < 3:
        return 1
    else:
        return Narayanascows(n - 3) + Narayanascows(n - 1)


print(Narayancows(n))
