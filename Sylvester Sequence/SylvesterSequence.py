#########################
## Sylvester Sequence  ##
#########################


#Example : 2 3 7 43 1807 3263443 ....

def seq(n):
        pdt = 1
        ans = 2
        N = 1000000007
        for i in range(1,n+1):
                ans = ((pdt % N) * (ans % N)) % N
                pdt = ans
                ans = (ans + 1) % N
        return ans

find_val = int(input("Enter the nth value to find : "))
print(find_val,"th value in Sylvester's Sequence is ",seq(find_val))
