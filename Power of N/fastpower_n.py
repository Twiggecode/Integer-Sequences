def fastpower(x, n): 
    """
    implement a fast power algorithm
    x : any float number, which works in python2 and 3
    n : any integer including negative
    """
    if(x == 0):
        return 0.
    
    if(n == 0):
        return 1.0
    # when n < 0, convert it to positve by taking the reciprocal of x
    if(n < 0):
        x = 1 / x
        n = abs(n)

    if(n % 2 == 0):
        return fastpower(x, n // 2) ** 2
    else:
        return fastpower(x, (n - 1) // 2) ** 2 * x

if __name__ == "__main__":
    x = float(input("Please input the base: "))
    n = int(input("Please input the power(int): "))

    if(x == 0. and n == 0):
        print("0 to the power of 0 is undefined")
    else:
        print("{} to the power of {} is : {}".format(x, n, fastpower(x, n)))
