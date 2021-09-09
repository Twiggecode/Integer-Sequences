MAX=100000
def Kaprekar_nums(n):
    arr=[]
    if n==0:
        return 1
    else:
        for i in range(0,MAX):
            
            # Get the digits from the square in a list:
            sqr = i ** 2
            digits = str(sqr)

            # Now loop from 1 to length of the number - 1, sum both sides and check
            length = len(digits)
            for x in range(1, length):
                left = int("".join(digits[:x]))
                right = int("".join(digits[x:]))
                if (left + right) == i:
                    arr.append(i)
        return arr[n-1]
val=int(input("enter the nth value to find int he Kaprekar series : "))
print(str(val)+" th value in Kaprekar's number series is :",Kaprekar_nums(val))