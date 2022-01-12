
"""
    A Star Number is a centered figurate number a centered hexagram (six-pointed star),
    such as the Star of Divid, or the board Chinese Checkers is played on.
    
    The nth star number is given by the formula Sn = 6n(n - 1)+1.
    EX: 1, 13, 37, 73, 121, 181, 253, etc...
    Ref: https://en.wikipedia.org/wiki/Star_number
"""
def star_number(n: int) -> int:
    # if the input is 0 or 1 then output remains same as the input
    if n <= 1:
        return n
    
    # return the output of the above formula
    return 6 * n * (n - 1) + 1

if __name__ == "__main__":
    try:
        n = int(input("Enter your input to get the nth star number : "))
        if n < 0:
            raise ValueError("Your input must be greater than 0")
        else:
            result = star_number(n)
            print(f'The {n}th star number is : {result}')
    except ValueError:
        print("You must enter an Integer number")
