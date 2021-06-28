# The nth element in the sequence
def user_input():
    n = int(input("Enter the value of n: "))
    return n


def tribonacci(): 
    # Initialize the first three sequence values
    a, b, c = 0, 0, 1

    n = user_input()  
    for i in range(n - 3):
        d=a+b+c
        a=b
        b=c
        c=d
    return d

if __name__ == "__main__":
    print (f'The Nth term in the sequence is {tribonacci ()}')
