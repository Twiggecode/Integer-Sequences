MAX = 10000
def ulam(n):
        if(n == 0):
                return n
        
        arr = []
        s = set()

        arr.append(1)
        arr.append(2)
        
        s.add(1)
        s.add(2)

        for i in range(3, MAX):
                count = 0
                for j in range(0, len(arr)):
                        if(i - arr[j] in s and arr[j] != (i - arr[j])):
                                count += 1
                        if(count > 2):
                                break
                if(count == 2):
                        arr.append(i)
                        s.add(i)
        return arr[n-1]
                        
        
#Example : 1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102        


find_val = int(input("Enter the nth value to find : "))
print(find_val,"th value in Ulam's Sequence is ", ulam(find_val))
