// CPP program to print fermat numbers
#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;
#define llu int128_t
using namespace std;
 
/* Iterative Function to calculate (x^y) in O(log y) */
llu power(llu x, llu y)
{
    llu res = 1; // Initialize result
 
    while (y > 0) {
        // If y is odd, multiply x with the result
        if (y & 1)
            res = res * x;
 
        // n must be even now
        y = y >> 1; // y = y/2
        x = x * x; // Change x to x^2
    }
    return res;
}
 
// Function to find nth fermat number
llu Fermat(llu i)
{
    // 2 to the power i
    llu power2_i = power(2, i);
 
    // 2 to the power 2^i
    llu power2_2_i = power(2, power2_i);
 
    return power2_2_i + 1;
}
 
// Function to find first n Fermat numbers
void Fermat_Number(llu n)
{
     
    for (llu i = 0; i < n; i++) {
         
        // Calculate 2^2^i
        cout << Fermat(i);
         
        if(i!=n-1)
            cout << ", ";
    }
}
 
// Driver code
int main()
{
    llu n = 7;
     
    // Function call
    Fermat_Number(n);
 
    return 0;
}
