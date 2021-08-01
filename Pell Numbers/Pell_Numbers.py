#################################
###     Pell Numbers          ###
#################################


def pellNumbers(n):
    if n <= 2:
        return n
    first = 1
    second = 2
    for i in range(3, n + 1):
        tmp = 2 * second + first
        first, second = second, tmp
    return second


find_val = int(input("Enter the nth value : "))
print(find_val, "th value in Pell Number is ", pellNumbers(find_val))
