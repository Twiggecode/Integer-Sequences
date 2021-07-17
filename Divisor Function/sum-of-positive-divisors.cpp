#include <math.h>
#include <iostream>

/*  Returns the sum of the positive divisors of n.

    @param The integer n.
    @return The sum of positive numbers that divide n.
*/
const int sumOfPositiveDivisors(const int& n)
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
            // If i * i = n, add the divisor by itself
            if (n / i == i)
            {
                sum += i;
            }
            else
            {
                sum += i + (n / i);
            }
        }
    }

    // Add divisors n and 1 to the result
    return sum + n + 1;
}

/*      DRIVER CODE     */
int main()
{
    // int number = 100;

    /*std::cout << "sigma(" << number << ") = " << sumOfPositiveDivisors(number)
        << std::endl;*/

    for (int i = 1; i <= 50; i++)
    {
        std::cout << "sigma(" << i << ") = " << sumOfPositiveDivisors(i)
            << std::endl;
    }

    return 0;
}
