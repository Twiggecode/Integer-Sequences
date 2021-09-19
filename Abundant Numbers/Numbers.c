#include <stdio.h>

void printAbundantNumbers(int start, int stop);
//int returnIfAbundant();
//int returnAbundantNumber();

int main() {
    printf("Enter your starting number: ");
    int start;
    scanf("%d", &start);

    printf("Enter your stopping number: ");
    int stop;
    scanf("%d", &stop);

    printAbundantNumbers(start, stop);

    // printf("Enter the number to check for abundance: ");
    // int checkAbundance;
    // scanf("%d", &checkAbundance);

    return 0;
}

/**
 * This will print all abundant number between
 * star and stop. A number is abundant if
 * sum(m) > 2m: where sum(m) is the summation of all
 * the divisors of m.
 */
void printAbundantNumbers(int startNum, int stopNum) {
    while (startNum <= stopNum) {
        int divisors = 0;

        for (int i = 1; i < startNum + 1; ++i) // Iterate all possible divisords.
            divisors += (startNum % i == 0) ? i : 0; // Checks if i is a divisor and sums it.

        if (divisors > (2 * startNum)) // Prints if abundance is met.
            printf("%d is abundant\n", startNum);

        ++startNum;
    }

}

