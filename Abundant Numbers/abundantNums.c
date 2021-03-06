#include <stdio.h>
/**
 * printAbundantNumbers()
 * Calculates and prints all abundant numbers between a start and stop value.
 *
 * printDeficientNumbers()
 * Calculates and prints all deficient numbers between a start and stop value.
 *
 * returnIfAbundant()
 * Will return an int 1 (true) if a passed number is abundant and an int 0
 * (false) if a passed number is not abundant.
 *
 * A number is abundant if sum(m) > 2m, where sum(m) is the summation of all
 * of m's divisors. A deficient is opposite of an abundant number:
 * sum(m) < 2m
 */

// Functions declarations
//
// Get numbers from user functions
void getStartStop(int*, int*);
void getCheckNum(int*);

// Abundant number functions
void printAbundantNumbers(int, int);
int returnIfAbundant();

// Deficient number functions
void printDeficientNumbers(int, int);

int main() {
    // Initialize variables for print function
    int start, stop;

    // Function to get user's range of numbers
    getStartStop(&start, &stop);

    // Prints abundant numbers in the range start - stop
    printAbundantNumbers(start, stop);

    // Prints deficient numbers in the range start - stop
    printDeficientNumbers(start, stop);

    // Initialize variable for Abundance check
    int checkAbundance;

    // Function to get user's number
    getCheckNum(&checkAbundance);

    // Returns 1 or 0 based on abundance
    int isAbundant = returnIfAbundant(checkAbundance);

    // Prints a 1 if the passed number is abundant
    printf("%d\n", isAbundant);

    return 0;
}

/**
 * This will print all abundant numbers between
 * start and stop. A number is abundant if
 * sum(m) > 2m, where sum(m) is the summation of all
 * the divisors of m.
 */
void printAbundantNumbers(int startNum, int stopNum) {
    while (startNum <= stopNum) {
        int divisors = 0;

        for (int i = 1; i < startNum + 1; ++i) // Iterate all possible divisors.
            divisors += (startNum % i == 0) ? i : 0; // Checks if i is a divisor and sums it.

        if (divisors > (2 * startNum)) // Prints if abundance is met.
            printf("%d is abundant.\n", startNum);

        ++startNum;
    }
}

/**
 * Returns a 1 if the passed num is abundant.
 * Returns a 0 if the passed num is not abundant.
 */
int returnIfAbundant(int num) {
    int divisors = 0;

    for (int i = 1; i < num + 1; ++i) // Iterate all possible divisors.
        divisors += (num % i == 0) ? i : 0; // Checks if i is a divisor and sums it.

    return divisors > (2 * num);
}

/**
 * This will print all deficient numbers between
 * start and stop. A number is deficient if
 * sum(m) < 2m, where sum(m) is the summation of all
 * the divisors of m. (Note: It's the opposite of an
 * abundant number)
 */
void printDeficientNumbers(int startNum, int stopNum) {
    while (startNum <= stopNum) {
        int divisors = 0;

        for (int i = 1; i < startNum + 1; ++i) // Iterate all possible divisors.
            divisors += (startNum % i == 0) ? i : 0; // Checks if i is a divisor and sums it.

        if (divisors < (2 * startNum)) // Prints if deficiency is met.
            printf("%d is deficient.\n", startNum);

        ++startNum;
    }
}

/**
 * Prompts user for the starting and stoping number
 * to check for abundance in a range of numbers
 */
void getStartStop(int* pStart, int* pStop) {
    printf("Enter your starting number: ");
    scanf("%d", &*pStart);

    printf("Enter your stopping number: ");
    scanf("%d", &*pStop);
}

/**
 * Prompts the user to enter a number they want
 * checked for abundance
 */
void getCheckNum(int* pCheckNum) {
    printf("Enter the number to check for abundance: ");
    scanf("%d", &*pCheckNum);
}

