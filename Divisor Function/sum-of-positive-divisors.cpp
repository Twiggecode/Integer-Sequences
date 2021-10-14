#include <math.h>
#include <iostream>


/*  Returns an integer a raised to the power of b.
*   @param  The integer to exponentially raise, and the
*           power integer.
*
*   @return 1 if b = 0, if b is even (a^b/2 * a^b/2), else (a^b/2 * a^b/2 * a)
*/
const int fastPower(const int& a, const int &b)
{
    if( b == 0)
    {
        return 1;
    }

    //calculate a^b/2 once and use it to calculate recursive a^n
    int half = fastPower(a, b/2);

    //check if b is even or odd
    if(b & 1) // b % 2
        return half * half * a;
    
    return half * half;
}

/*  Returns the sum of the kth powers of the positive divisors of n.
*
*   @param  The integer n, and the kth power integer.
*   @return The sum of the kth powers of positive numbers that
*           divide n.
*/
const int sumOfPositiveDivisors(const int& n, const int& k)
{
    int sum = 0;

    if (n <= 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }

    /* from http://www.pitt.edu/~bonidie/cs441/primes.pdf:
    *  If n is a composite integer, then it has two positive integer
    *  factors a and b, where 1 < a <= b < n. By proof of
    *  contradiction, either a <= sqrt(n) or b <= sqrt(n).
    *
    *  Therefore, the search limit for divisors can be set to sqrt(n).
    *  To get the sum of divisors > sqrt(n), divide n by i, where
    *  1 < i <= sqrt(n).
    */
    double limit = sqrt(n);
    for (int i = 2; i <= limit; i++)
    {
        if (n % i == 0)
        {
            // If i * i = n, add i^k by itself
            if (n / i == i)
            {
                sum += fastPower(i, k);
            }
            else
            {
                sum += fastPower(i, k) + fastPower(n / i, k);
            }
        }
    }

    // Add divisors n^k and 1 to the result
    return sum + fastPower(n, k) + 1;
}

/*      DRIVER CODE     */
int main()
{
    int x = 1;

    for (int i = 1; i <= 50; i++)
    {
        std::cout << "sigma_" << x << "(" << i << ") = "
            << sumOfPositiveDivisors(i, x) << std::endl;
    }

    return 0;
}
