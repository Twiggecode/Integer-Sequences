// C++ implementation of Juggler Sequence
#include <iostream>
#include <cmath>
#include <math.h>
 
// This function prints the juggler Sequence
void printJuggler(long long n) {
    
    long long a = n;
 
    // print the first term
    std::cout << a << " ";
 
    // calculate terms until
    // last term is not 1
    while (a != 1)
    {
        long long b = 0;
 
        // Check if previous term
        // is even or odd
        if (!(a % 2)){
 
            // calculate next term
            b = floor(sqrt(a));
            
        }
 
        else{ 
 
            // for odd previous term
            // calculate next term
            b = floor(sqrt(pow(a, 3.0)));

        }
        std::cout << b << " ";
        a = b;
    }
}
 
// Driver Code
int main() {
    int n;
    
    std::cin >> n; // enter the starting number for the Sequence

    printJuggler(n);

}
