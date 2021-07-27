##############################
##      Euclid–Mullin       ##
##############################

#Formula : a(1) = 2; a(n + 1) is smallest prime factor of a(1) a(2) ⋯ a(n) + 1.
#Example : 2,3,7,43,13,53,5,6221671,38709183810571,139,2801,11,17,5471....


def smallPrimeFactor(n):
        i = 2
        while(( i * i) <= n):
                if(n%i == 0):
                        return i
                i += 1
        return n

def EuclidMullin(n):
        product = 1
        for i in range(0,n):
                ans = smallPrimeFactor(product + 1)
                product *= ans
        return ans

find_val = int(input("Enter the nth Value to find : "))
print(f"{find_val}th value in Euclid-Mullin sequence is {EuclidMullin(find_val)}")