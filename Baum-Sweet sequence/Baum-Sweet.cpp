#include <iostream>
#include <bitset>
#include <string>


//the nth term of the sequence is 1 if the number n has no odd number of contiguous zeroes in its binary representation, else the nth term is 0.
//n:          0,1,2,3,4,5,6,7
//value at n: 0,1,0,1,1,0,0,1

//source: https://www.geeksforgeeks.org/baum-sweet-sequence/

int nthBaumSweetSeq(int n) {
  //number of bits in biteset
  const int bitset_size = 32;

  // bitset stores bitwise representation of n
  std::bitset<bitset_size> bs(n);
  
  // len stores the number of bits in the 
  // binary of n. builtin_clz() function gives 
  // number of zeroes present before the 
  // leading 1 in binary of n
  int len = bitset_size - __builtin_clz(n);
  
    
  for (int i = 0; i < len;) {
      int j = i + 1;
  
      //enter into a zero block
      if (bs[i] == 0) {
          int cnt = 1;
          //loop through zero block and count the length
          for (j = i + 1; j < len; j++) {
              // counts consecutive zeroes 
              if (bs[j] == 0)                   
                  cnt++;
              else
                  break;
            }
  
            //if length of zero block is odd -> nth term is 0
            if (cnt % 2 == 1)
                return 0;
        }
        i = j;
    }
  //if no zero block with odd lenght -> nth term is 1
  return 1;
}


//Driver Code
int main() {
    int n;
    std::cout<< "Enter the index (n) of the value: ";
    std::cin>> n;

    std::cout<< "The term at the required index of the Baum-Sweet sequence is: ";
    std::cout<< nthBaumSweetSeq(n);
}
