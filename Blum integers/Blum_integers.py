#This is a program to get the nth term of sequence of Blum integers.
#Blum integers are numbers of the form pq where p and q are distinct primes congruent to 3 (mod 4).
#for more info on blum integers checkout its wikipedia page
#time taken is low  for blum integer upto 2^19 (i.e. upto approx 26000th term)
import math #imported math library
def blum_integer(n):
    #first we define a function to check if 
    #a number is a blum integer
    def condition(num):
        #omega and big_omega are the funtions of number theory
        #check on wiki for detailed description of omega functions
        
        
        omega=set()              #omega has distinct primes only so a set is used
        big_omega=[]             #big_omega has all prime numbers
        
        #a loop for prime factorisation of number and getting onega and big_omega
        while num % 2 == 0:
            num = num / 2
            omega.add(2)
            big_omega.append(2)
        for i in range(3,int(math.sqrt(num))+1,2):
            while num % i== 0:
                num = num / i
                omega.add(i)
                big_omega.append(i)
        if num>2:
            omega.add(num)
            big_omega.append(num)
            
        # here we return a list of three items 
        #omega function, big_omega function and distinct primes that omega contains
        return [len(omega),len(big_omega),omega]
    
    k=0
    # here k represents the term number(to get nth term)
    x=1
    # here x represent the n term value 
    
    #a loop to evaluate n th term
    while k!=n+1:
        #condition are ordered in a sequence to reduce time complexity
        if (condition(x)[0]==2) & (condition(x)[1]==2) & ([i%4 for i in condition(x)[2]]==[3,3]):
            k+=1
        else:
            pass
        x+=4
    return x-4               #x-4 is used as last statement(x+=4) increases result by 4 one time extra

#here we call the function
n_term=int(input('enter the value for n(>=0): '))
blum_integer(n_term)
