#include <stdio.h>

int main() {
    int isItAbundant = 18;
    int sumDivisors = 0;

    for (int i = 1; i < (isItAbundant + 1); ++i) {
        if (isItAbundant % i == 0) {
            sumDivisors += i;
        }
    }

    printf("%d - %d - %d\n", sumDivisors, isItAbundant, 2 * isItAbundant);

    if (sumDivisors > (2 * isItAbundant)) {
        printf("%d is Abundant\n", isItAbundant);
    }
    else if (sumDivisors == isItAbundant) {
        printf("%d is Perfect\n", isItAbundant);
    }
    else if (sumDivisors < (2 * isItAbundant)) {
        printf("%d is Deficient\n", isItAbundant);
    }
    else {
        printf("ERROR\n");
    }

    return 0;
}
