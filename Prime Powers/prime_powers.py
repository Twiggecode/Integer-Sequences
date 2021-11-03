import math

def is_prime_power(n):
   #even number divisible
   factors = set()
   while n % 2 == 0:
      factors.add(2)
      n = n / 2
    
   #n became odd
   for i in range(3,int(math.sqrt(n))+1,2):
      while (n % i == 0):
         factors.add(i)
         n = n / i
    
   if n > 2:
       factors.add(n)
   return len(factors) == 1

def main():
    n = int(input('Enter n: '))
    count = -1
    curr = 0
    while count < n:
        curr += 1
        if is_prime_power(curr):
            count += 1
    print(curr)

if __name__ == '__main__':
    main()
