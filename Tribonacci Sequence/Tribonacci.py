# This code will return the nth element of the Tribonacci sequence

def tribonacci(n,mem={}):
    if(n==0 or n==1):
        mem[n]=0
        return mem[n]
    elif(n==2 or n==3):
        mem[n]=1
        return mem[n]

    if(n in mem.keys()):
        return mem[n]

    mem[n]=tribonacci(n-3)+tribonacci(n-2)+tribonacci(n-1)
    return mem[n]
    

if __name__ == "__main__":
    n=int(input("Enter the value of n: "))
    print(f"The Nth term in the sequence is {tribonacci (n,)}")