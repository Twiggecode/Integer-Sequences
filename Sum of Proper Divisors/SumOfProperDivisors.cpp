/*

    C++ Program to find the sum of proper divisors of the nth number.

*/

#include <bits/stdc++.h>
using namespace std;

int findDivSum(int n) {
    if (n == 1) return 0;
    
    int sum = 1;
    int i = 2;

    while (i * i <= n) {
        if (n % i == 0) {   // check if a number is a divisor of n
            sum += i;
            if (n / i != i) { // check if n is a perfect square
                sum += n / i;
            }
        }
        i += 1;
    }

    return sum;
}

// Main Function
int main()
{
    int n;

    cout<< "Enter a number: ";
    cin>> n;
    cout<< "The " << n << "th number's proper divisors sum is: " << findDivSum(n) << "\n";

    return 0;
}
