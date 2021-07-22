def factorial(a:int):
    if a == 0:
        return 1
    elif a > 0:
        res = 1
        for el in range(1,a+1):
            res *= el
        return res
        
    else:
        return "Input Error! It has to be an integer in range of 0 and on"      





if __name__ == "__main__":
    n = int(input("Enter integer value: "))
    print("%d! = %d" %(n, factorial(n)))
    

