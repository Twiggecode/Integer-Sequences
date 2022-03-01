#include <stdio.h>

void green() {
	printf("\033[32m");
}

void reset() {
	printf("\033[0m");
}

unsigned long long findLucasNumber(unsigned long long index) {
    if (index == 0) return 2;
    if (index == 1) return 1;
    return findLucasNumber(index-1) + findLucasNumber(index-2);
}

int main() {
    unsigned long long index;
    printf("Lucas Number:\n");
    printf("    if n = 0 => Ln := 2:\n");
    printf("    if n = 1 => Ln := 1:\n");
    printf("    if n > 1 => Ln := Ln - 1 + Ln - 2:\n");
    printf("Enter the nth element of Lucas sequence: ");
    scanf("%llu",&index);
    printf("Lucas sequence: ");

    for (int i = 0; i <= index; i++) {
        if ( i == index ) {
            green();
            printf(" %llu",findLucasNumber(i));
            reset();
            printf(", ...");
        } else {
            printf(" %llu,",findLucasNumber(i));
        }
    }

   return 0;
}