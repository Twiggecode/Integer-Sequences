########################################
### Central Binomial Coefficient     ###
########################################

#Example : 1, 2, 6, 20, 70, 252, 924, 3432 ....
#Formula : Check Wikepedia


def coeff(n,k):
        c = [[0 for i in range(k+1)] for j in range(n+1)]
        for i in range(n+1):
                for j in range(min(i,k) + 1):
                        if(j == 0 or j == i):
                                c[i][j] = 1
                        else:
                                c[i][j] = c[i-1][j-1] + c[i-1][j]
        return c[n][k]


find_val = int(input("Enter the nth value to find : "))
print(find_val, "th value in Central Binomial Coefficiecnt is : ", coeff(2*find_val, find_val))
