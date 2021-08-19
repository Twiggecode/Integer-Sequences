from sympy import primorial

###############################
###     Primorials          ###
###############################

#Explanation : The product of the first n primes.
#Example : 1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, ...


n = int(input("Enter the nth value to find : "))
if(n == 0):
        print(n,"th primorial term is 1")
else:
        print(n,"th primorial term is ",primorial(n))
