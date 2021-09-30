/**
 * Algorithms to show, return and check if a number is a
 * Perfect Number. A perfect number, sum(m) == 2m; where
 * sum(m) is the summation of m's divisors, is a number whos
 * even divisors sum to twice the number (m).
 */
// TODO: Comment code
//
// The explanation and code of perfect number is incorrect
//
#include <stdio.h>

void printPerfects(int, int);
int checkIfPerfect(int);
// void nthPerfectNumber(int);

int main() {
    printPerfects(0, 9000);

    // int isItPerfect = 8128;
    // int itsPerfect = checkIfPerfect(isItPerfect);

    // if (itsPerfect)
    //     printf("%d is Perfect\n", isItPerfect);
    // else
    //     printf("%d is not Perfect\n", isItPerfect);

    return 0;
}

void printPerfects(int start, int stop) {
    while (start <= stop) {
        int divisors = start;

        for (int i = 1; i < (start / 2) + 1; ++i)
            divisors += (start % i == 0) ? i : 0;

        if (divisors == 2 * start)
            printf("%d is Perfect\n", start);

        ++start;
    }
}

int checkIfPerfect(int n) {
    int divisors = n;

    for (int i = 1; i < (n / 2) + 1; ++i)
        divisors += (n % i == 0) ? i : 0;

    return (divisors == 2 * n) ? 1 : 0;
}

