store = dict()

def Wedderburn(n):
     
    # Base case
    if (n <= 2):
        return store[n]
 
    # If n is even n = 2x
    elif (n % 2 == 0):
         
        # get x
        x = n // 2
        ans = 0
 
        # a(2x) = a(1)a(2x-1) + a(2)a(2x-2) + ... +
        # a(x-1)a(x+1)
        for i in range(1, x):
            ans += store[i] * store[n - i]
 
        # a(x)(a(x)+1)/2
        ans += (store[x] * (store[x] + 1)) // 2
 
        # Store the ans
        store[n] = ans
 
        # Return the required answer
        return ans
    else:
         
        # If n is odd
        x = (n + 1) // 2
        ans = 0
 
        # a(2x-1) = a(1)a(2x-2) + a(2)a(2x-3) + ... +
        # a(x-1)a(x),
        for i in range(1, x):
            ans += store[i] * store[n - i]
 
        # Store the ans
        store[n] = ans
 
        # Return the required answer
        return ans
 
n = int(input("Enter the nth value to find : "))
store[0] = 0
store[1] = 1
store[2] = 1
for i in range(n+1):
        Wedderburn(i)
print(store[n])
