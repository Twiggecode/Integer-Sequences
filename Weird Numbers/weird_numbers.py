         divisors.extend([i,int(n/i)])
        i += 1
    divisors.remove(n)
    divisors.sort()
    return divisors

def subset_generator(arr):
@@ -21,15 +20,13 @@ def subset_generator(arr):
            yield elem

def isWeird(num):
    isSemiPerfect = False
    isAbundant = False
    divisors = find_divisors(num)
    if sum(divisors) > num:
        isAbundant = True
    if not (sum(divisors) > num):
        return False
    for subset in subset_generator(divisors):
        if sum(subset) == num:
            isSemiPerfect = True
    return isAbundant and not isSemiPerfect
            return False
    return True

def main():
    n = int(input('Enter n: '))
@@ -45,9 +42,3 @@ def main():
