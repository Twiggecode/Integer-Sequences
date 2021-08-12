print("This programs finds the nth term in the alternating sequence")
n=int(input("Enter the nth term whoose value you want to find"))

def find_fac(n):
    if(n==1):
        return(1)
    else:
        return(n*find_fac(n-1))

def alternating_fac(n):
    if(n==0 or n==1):
        return 1
    term=0
    flag_to_sub=0
    n=n+1
    while(n>0):
        if( flag_to_sub):
            term=term-(find_fac(n))
            flag_to_sub=0
        else:
            term=term+(find_fac(n))
            flag_to_sub=1

        n=n-1
        # print("Term",term)

    return term
        
            


print(alternating_fac(n))