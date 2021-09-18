#include <iostream>

/*
- PRIME MUNBERS -
Example:
Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
Is_Prime(21) --> will return 'false' value
Is_Prime(7) --> will return 'true' value
*/

// Boolean function that returns true if the input is Prime, else returns false
bool Is_Prime(int n) {

    // If less than 2, or even number, and not 2 --> not prime
    if (n < 2 || (n % 2 == 0 && n!=2))
        return false;

    // 2 is prime
    if (n == 2)
         return true;

    /**
      Iterate from 3 to half the user's entered number.
      Once we are above half of the entered number (n) no
      number divides evenly into n and it's therefore prime.
      We start at 3 since we have already checked if n = 2.
      We increment by 2 since we have already checked if the
      number is even.
    */
    for (int i = 3; i < (n / 2); i += 2)
        if (n % i == 0)
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
