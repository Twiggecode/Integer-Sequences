/*
Compile Instructions:
In order to compile this code use must link the math library.
Example: gcc JacobsthalNumbers.c -o exec -lm
*/
#include <stdio.h>
#include <math.h>

#define BASE 2
#define DENOMINATOR 3

void green() {
	printf("\033[32m");
}

void reset() {
	printf("\033[0m");
}

unsigned long long myPow(unsigned long long n) {
    int i;
    int number = 1;

    for (i = 0; i < n; ++i)
        number *= BASE;

    return(number);
}

void findJacobsthalNumber(unsigned long long index) {
    unsigned long long firstTerm, secondTerm, numerator, endResult;
    printf("Jacobsthal sequence: ");
    for (unsigned long long i = 0; i <= index; ++i) {
        firstTerm = myPow(i);
        secondTerm = i % 2 == 0 ? 1 : -1;
        numerator = firstTerm - secondTerm;
        endResult = numerator / DENOMINATOR;
        if ( i == index) {
            green();
            printf(" %llu", endResult);
            reset();
            printf("...\n");
        } else {
            printf(" %llu ", endResult);
        }
    }
}

int main() {
    unsigned long long index;
    printf("Jacobsthal Number: J_n = ( 2^n - (-1)^n ) / 3\n");
    printf("Enter the nth element of Jacobsthal sequence: ");
    scanf("%llu",&index);
    findJacobsthalNumber(index);
   return 0;
}