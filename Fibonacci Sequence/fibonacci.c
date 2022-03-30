#include <stdio.h>

typedef unsigned long long U64;

U64 fibonacci(U64 n);

// print the nth element of the fibonacci sequence. n should be a non-negative integer
int main()
{
    U64 n;
    printf("Please enter a non-negative integer: ");
    scanf("%llu", &n);
    // fibonacci(3);

    printf(
        "%lluth element of fibonacci sequence = %llu\n",
        n,
        fibonacci(n)
    );

    return 0;
}

/**
 * return the nth element of the fibonacci sequence. n should be a non-negative integer
 *
 * @param n the element to find
 * @return the nth element of the fibonacci sequnce
 */
U64 fibonacci(U64 n)
{
    if (n == 0) {
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    else {
        U64 t1 = 0;
        U64 t2 = 1;

        // TODO: check for integer overflow
        U64 result, temp;
        for (U64 i = 1; i <= n - 1; ++i) {
            result = t1 + t2;

            temp = t2;
            t2 = result;
            t1 = temp;
        }

        return result;
    }
}
