// Iterative C/C++ program
// to find n'th Lucas Number
// Optimised to work in O(n) time complexity
#include <stdio.h>
 
// Iterative function
int lucas(int n)
{
    // declaring base values
    // for positions 0 and 1
    int a = 2, b = 1, c, i;
 
    if (n == 0)
        return a;
 
    // generating number
    for (i = 2; i <= n; i++)
    {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}
 
// Driver Code
int main()
{
    int n = 9;
    printf("%d", lucas(n));
    return 0;
}