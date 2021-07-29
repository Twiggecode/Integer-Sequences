// C program for calculating x raised to the power of y 
// Time complexity O(log(n))

#include <stdio.h>

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
    printf("Enter x in x^y: ");
    scanf("%llu", &x);
    printf("Enter y in x^y: ");
    scanf("%llu",&y);
    printf("%llu to power %llu is: %llu ",x,y,power(x,y));
    return 0;
}
 
