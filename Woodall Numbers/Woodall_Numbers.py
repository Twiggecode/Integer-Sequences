#####################################
###     Woodall Numbers           ###
#####################################

# Formula: n*2n − 1, with n ≥ 1.
# Example : {1, 7, 23, 63, 159, 383, 895, 2047, 4607, ...}
# Input of 0 for n = 1, 1 for n = 2...
find_val = int(input("Enter the nth value : "))
print(
    find_val,
    "th value of Woodall Number is ",
    (find_val + 1) * (2 ** (find_val + 1)) - 1,
)
