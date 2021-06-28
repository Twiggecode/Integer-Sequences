# This code will return the nth element of the Tribonacci sequence

def user_input():
    n = int(input("Enter the value of n: "))
    n = n+1
    return n


def tribonacci(): 
    # Initialize the first three sequence values
    a, b, c = 0, 1, 1

    n = user_input()  
    
    if n==1:  # return the 0th element of the sequence for input=0
        
        return 0
    
    elif n==2 or n==3:  # the next two elements of the sequence are both 1, so return 1 for input=1 and input=2
        
        return 1
    
    else:   # else we use the equation Tn = Tn-1 + Tn-2 + Tn-3
    
    
        for i in range(n - 3):
            d=a+b+c
            a=b
            b=c
            c=d
        return d

if __name__ == "__main__":
    print (f'The Nth term in the sequence is {tribonacci ()}')
