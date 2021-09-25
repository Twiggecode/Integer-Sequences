from scipy.special import euler

n = int(input("Input: "))

print(round(euler(n)[-1]))