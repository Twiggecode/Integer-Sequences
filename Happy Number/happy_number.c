#include <stdio.h>
#include <math.h>

//This algorithm determines if a number n is happy number.

int main()
{
    bool isHappy(int n)
    {
    
    int recur, n, sum = 0;
    
    scanf("Enter number: %s", n);

    // Returning 1 and 7 as true because 7 is a happy number
    if (n == 1 || n == 7)
    {
        printf("true");
    }    
    else if (n < 10 && n != 1)
    {
        printf("false");
    }

    // Loop to square each digit and then add them
    while(n > 0)
    {
        sum += pow((n % 10), 2);
        n = n / 10;
    }
    
    // Calling the isHappy function till the number is single digit.
    recur = isHappy(sum);
    
    if (recur == 1 || recur == 7)
    {
        printf("true");
    }
    return false;
    }    
    return 0;
}