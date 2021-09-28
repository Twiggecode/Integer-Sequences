/**
 * Algorithms to show, return and check if a number is a
 * Perfect Number. A perfect number, sum(m) == 2m; where
 * sum(m) is the summation of m's divisors, is a number whos
 * even divisors sum to twice the number
 */
// TODO: Comment code
#include <stdio.h>

void printPerfects(int, int);

int main() {
    printPerfects(0, 100000);

    return 0;
}

void printPerfects(int start, int stop) {
    while (start <= stop) {
        int divisors = 0;

        for (int i = 1; i < (start / 2) + 1; ++i)
            divisors += (start % i == 0) ? i : 0;

        divisors += start;

        if (divisors == (2 * start))
            printf("%d is Perfect\n", start);

        ++start;
    }
}
