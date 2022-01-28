/*
Compile Instructions:
In order to compile this code use must link the math library.

Example: gcc fermat_numbers.c -o exec -lm
*/
#include <stdio.h>
#include <math.h>

int main()
{
    unsigned long long  base = 2, power, innerPower, endResult;
    printf("Fermat Numbers Sequence: F_n = 2 ^ (2^n) + 1\n");
    printf("Enter the power raised (n): ");
    scanf("%llu",&power);

    innerPower = pow(2,power); // Calculate 2 ^ n

    endResult = pow(2,innerPower) + 1; // Calculate 2 ^ result + 1

    printf("Result: 2 ^ (2^%llu) + 1 = %llu\n", power, endResult);

    return 0;
}