###############################
###   Jacobsthal Numbers    ###
###############################

#Forumula: J(n) = J(n-1)+2*J(n-2)
#Example:  0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, 10923, 21845, 43691, ……


def Jacobsthal(n):
        dp = [0] * (n+2)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
                dp[i] = dp[i-1] + 2 * dp[i-2]

        return dp[n]


find_val = int(input("Enter the nth value : "))
print(find_val,"th value of Jacobsthal Number is ",Jacobsthal(find_val))
