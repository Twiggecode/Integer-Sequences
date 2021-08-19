#pragma once
#include <iostream>

/*
- PRIME MUNBERS - 
Example:
Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
Is_Prime(21) --> will return 'false' value
Is_Prime(7) --> will return 'true' value
*/

// Boolean function that retutn TRUE if the input is Prime, else return FALSE
bool Is_Prime(int n) {

    if (n <= 1 || (n % 2 == 0 && n!=2))               // If less than 2, or even number, and not 2 --> not prime
        return false;

    if (n == 2)                                    // 2 is prime
         return true;

    for (int i = n / 2 + 1; i > 1; i = i - 2)     // Any valid divisor, if exist, must be odd and <= n\2 
        if (!(n % i))
            return false;

    return true;
}

int main() {
  int n;

  std::cout<<"Enter an integer greater than 1: ";
  std::cin>>n;

  Is_Prime(n);
  if(Is_Prime(n)==true){
    std::cout<<"True";
  }else{
    std::cout<<"False";
  }
}