###############################
###     Perrin Sequence     ###
###############################

# Perrin Sequence Explanation
# P(n) = P(n−2) + P(n−3) for n ≥ 3, with P(0) = 3, P(1) = 0, P(2) = 2.
# Example : {3, 0, 2, 3, 2, 5, 5, 7, 10, 12, ...}


def Perrin_Seq(n):
    first = 3
    second = 0
    third = 2
    if n == 0:
        return first
    if n == 1:
        return second
    if n == 2:
        return third
    while n > 2:
        tmp = first + second
        first, second, third = second, third, tmp
        n -= 1
    return tmp


find_val = int(input("Enter the nth value : "))
print(find_val, "th value in Perrin Sequence is ", Perrin_Seq(find_val))
