#include <stdio.h>

int main() {
    int isItAbundant = 1;
    int max = 271;

    do
    {
        int sumDivisors = 0;

        for (int i = 1; i < (isItAbundant + 1); ++i)
            sumDivisors += (isItAbundant % i == 0) ? i : 0;

        if (sumDivisors > (2 * isItAbundant))
            printf("%d is Abundant\n", isItAbundant);
        else if (sumDivisors == (2 * isItAbundant))
            printf("%d is Perfect\n", isItAbundant);
        else if (sumDivisors < (2 * isItAbundant))
            printf("%d is Deficient\n", isItAbundant);
        else
            printf("ERROR\n");

    } while (++isItAbundant < max);

    return 0;
}

