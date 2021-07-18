# Divisor Function

The divisor function ***sigma_k(n)*** is defined as the sum of the ***k***th powers of positive divisors of integer ***n***.

# Example

- ***sigma_0(14) = 1^0 + 2^0 + 7^0 + 14^0 = 1 + 1 + 1 + 1 = 4***
- ***sigma_1(30) = 1^1 + 2^1 + 3^1 + 5^1 + 6^1 + 10^1 + 15^1 + 30^1 = 72***
- ***sigma_3(6) = 1^3 + 2^3 + 3^3 + 6^3 = 1 + 8 + 27 + 216 = 252***

# Some Properties

- If ***k = 0***, that is ***sigma_0(n)***, then the function returns the number of divisors of ***n***.
- If ***k = 1***, that is ***sigma_1(n)***, then the function returns the sum of all divisors of ***n***.
- For a prime number ***p***,
  - ***sigma_0(p) = 1^0 + p^0 = 1 + 1 = 2***
  - ***sigma_1(p) = 1^1 + p^1 = p + 1***
  - ***sigma_0(p^n) = 1^0 + (p^1)^0 + (p^2)^0 + ... + (p^n)^0 = 1 + n * 1 = n + 1***
