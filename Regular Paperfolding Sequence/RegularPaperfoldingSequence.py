#####################################
## Regular Paperfolding Sequence   ##
#####################################

"""
Explanation:

        1 (starts with 1) 
 
        “1” 1 “0” 
        1 and 0 are inserted alternately to the left and right of the previous term. Here the number in the double quotes represents the newly added elements.
        So the second term becomes        1 1 0

        “1” 1 “0” 1 “1” 0 “0” 
        So the third term becomes         1 1 0 1 1 0 0 
 
        “1” 1 “0” 1 “1” 0 “0” 1 “1” 1 “0” 0 “1” 0 “0” 
        The fourth term becomes           1 1 0 1 1 0 0 1 1 1 0 0 1 0 0 


"""


def seq(n):
    s = "1"
    for i in range(2, n + 1):
        temp = "1"
        prev = "1"
        zero = "0"
        one = "1"

        for j in range(len(s)):
            temp += s[j]
            if prev == "0":
                temp += one
                prev = one
            else:
                temp += zero
                prev = zero
        s = temp
    return s


find_val = int(input("Enter the nth value to find : "))
print(find_val, "th value in Regular Paperfolding Sequence is ", seq(find_val))
