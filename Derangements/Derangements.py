 Derangements.py                                                                                                                                      
   1 def derangements(n):
   2     if n == 0:
   3         return 1
   4     if n == 1:
   5         return 0
   6     return (n-1) * (derangements(n-1) + derangements(n-2))
   7 n = int(input('Enter n: '))
   8 print(derangements(n))
   9 
  10 
~                                                                                                                                                     
~                                                                                                                                                     
~                                                         
