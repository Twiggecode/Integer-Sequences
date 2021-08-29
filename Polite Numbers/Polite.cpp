/*

    C++ Program to find the nth element of the Polite numbers where n is a positive integer input 
    by the user the polite numbers are the sequence of natural numbers that are not powers of 2

*/

#include <bits/stdc++.h>
using namespace std;

int findPoliteNumber(int n) {
    int i = 1;
    int count = 0;
    // count the first n natural numbers that are not powers of 2, which will return the nth polite number
    while (count <= n) {
        if ((log(i) / log(2)) != round((log(i) / log(2)))) // check if a number is not power of 2
            count++;
        i++; // count will not increment if the number is a power of 2
    }

    return i - 1;
}

// Main Function
int main()
{
    int n;

    cout<< "Enter a number: ";
    cin>> n;
    cout<< "The " << n << "th polite number is: " << findPoliteNumber(n) << "\n";

    return 0;
}
