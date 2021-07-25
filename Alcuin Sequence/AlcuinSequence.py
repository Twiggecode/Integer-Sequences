from math import floor

#Formula : a(n) = round(n^2/12) – floor(n/4)*floor((n+2)/4)
#Example : 0, 0, 0, 1, 0, 1, 1, 2, 1, 3, 2, 4, 3, 5, 4, 7 ....

def alcuin(n):
        return (round((n * n) / 12) - floor(n / 4) * floor((n + 2) / 4))

find_val = int(input("Enter the nth value to find : "))
print(find_val,"th value of Alcuin Sequence is ", alcuin(find_val))
