// C++ program for calculating x raised to the power of y 
// this is a non-iterative solution
// Time complexity O(log(n))
#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long U64;

U64 power(U64 x, U64 y)
{
    U64 result = 1;
    while (y > 0) {
        if (y % 2 == 0) // y is even
        {
            x = x * x;
            y = y / 2;
        }
        else // y isn't even
        {
            result = result * x;
            y = y - 1;
        }
    }
    return result;
}
 
// Driver Code
int main()
{   
    U64 x,y;
    cout<<"Enter x in x^y: ";
    cin>>x;
    cout<<"Enter y in x^y: ";
    cin>>y;
    cout << (power(x, y));
    return 0;
}
 
