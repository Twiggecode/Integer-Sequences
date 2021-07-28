############################
###     Motzkin numbers  ###
############################

#A given number n is the number of different ways of drawing non-intersecting chords between n points on a circle
#not necessarily touching every point by a chord. 
#Example : 1, 1, 2, 4, 9, 21, 51, 127, 323, 835, ...


def Motzkin(n):
        if(n == 0 or n == 1):
                return 1
        dp = [None]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
                dp[i] = ((2 * i + 1) * dp[i-1] + (3 * i - 3) * dp[i-2]) // (i+2)

        return dp[n]

find_val = int(input("Enter the nth value to find : "))
print(find_val,"th value in Motzkin numbers is ", Motzkin(find_val))
