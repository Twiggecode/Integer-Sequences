// C++ program for calculating x raised to the power of y 
// this is a non-iterative solution
// Time complexity O(log(n))
#include <bits/stdc++.h>
using namespace std;
 
int power(int x, int y)
{
    int result = 1;
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
    # just set the x,y to suit your needs
    int x,y;
    cin>>x>>y;
  
 
    cout << (power(x, y));
    return 0;
}
 
