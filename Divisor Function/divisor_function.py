power_of_function, dividend = input(
    "In the Function σ(n) base x enter the base and n respictively : "
).split()
divisor = []
for i in range(1, int(int(dividend) / 2) + 1):
    if (int(dividend) % i) == 0:
        divisor.append(i)
divisor.append(int(dividend))

sum = 0
for i in divisor:
    sum += i ** int(power_of_function)
print(
    "sum of positive divisors function σ x(n) where x is",
    power_of_function,
    "and n is",
    dividend,
    "is :",
    sum,
)
print("aliquot sum s(n) where n is", dividend, "is :", sum - int(dividend))
