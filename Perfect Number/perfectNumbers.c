/**
 * Algorithms to show, return and check if a number is a
 * Perfect Number. A perfect number, sum(n) == n (excludeing n)
 * is the summation of n's divisors, is a number whos even
 * divisors sum to the number (n). The number (n) is not
 * included in the summation.
 * These algorithsm are unable to calculate past the 5th
 * perfect number as such a number exceedes the size of a
 * int integer.
 * Calculations above the 4th perfect number (8132)
 * not reccommended.
 */
#include <stdio.h>

// Function definitions
void printPerfects(int, int);
int checkIfPerfect(int); // Requires a positive number greater than 1.
void nthPerfectNumber(int);

int main() {
    // Code to show results of functions
    printPerfects(0, 10000);

    puts("");

    int isItPerfect = 33550336;
    int perfectNumber = checkIfPerfect(isItPerfect);

    if (perfectNumber)
        printf("%i is Perfect\n", isItPerfect);
    else
        printf("%i is not Perfect\n", isItPerfect);

    puts("");

    isItPerfect = 33550335;
    perfectNumber = checkIfPerfect(isItPerfect);

    if (perfectNumber)
        printf("%i is Perfect\n", isItPerfect);
    else
        printf("%i is not Perfect\n", isItPerfect);

    puts("");

    nthPerfectNumber(4);

    return 0;
}

/**
 * Prints all perfect number from start to stop
 */
void printPerfects(int start, int stop) {
    // Iterate form star to stopt
    while (start <= stop) {
        // Set divisors summation value to 0
        int divisors = 0;

        // Check for perfect divisors, add to divisors if found
        // Stop half way to current start value as no perfect
        // divisors exist past the half of start value
        for (int i = 1; i <= (start / 2) + 1; ++i)
            divisors += (start % i == 0) ? i : 0;

        // Check if divisors sum is equal to the start value
        // print if it is true.
        // By definition perfect numbers are greater than 1.
        if ((divisors == start) && (start > 1))
            printf("%i is Perfect\n", start);

        // Goto the next number
        ++start;
    }
}

/**
 * Checks if the passed number is a perfect number
 * returns 1 if true 0 if false
 */
int checkIfPerfect(int n) {
    // Set divisors summation to 0
    int divisors = 0;

    // Iterate through all possible perfect divisors.
    // Check if it is a perfect divisor.
    // Add the divisor to divisor variable if it is perfect.
    // Stop half was to the passed number as there are no
    // perfect divisors beyond this point.
    for (int i = 1; i <= (n / 2) + 1; ++i)
        divisors += (n % i == 0) ? i : 0;

    // return 1 if perfect else return 0
    return (divisors == n) ? 1 : 0;
}

void nthPerfectNumber(int n) {
    int numPerfectNums = 0;
    int checkNum = 0;

    while (numPerfectNums < n) {
        int divisors = 0;

        ++checkNum;

        for (int i = 1; i <= (checkNum / 2) + 1; ++i)
            divisors += (checkNum % i == 0) ? i : 0;

        if ((divisors == checkNum) && (checkNum > 1))
            ++numPerfectNums;
    }

    printf("The %i-th perfect number is %i\n", n, checkNum);
}

