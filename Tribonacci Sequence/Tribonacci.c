#include <stdio.h>

typedef unsigned long long U64;

U64 main() {
    //Initialize first three Tribonacci sequence numbers
    U64 a = 0, b = 0, c = 1;
    
    //User input
    U64 n;
    printf("Enter the value of n: ");
    scanf("%llu",&n);
 
    //value for input 0 (first term) or input 1 (second term)
    if (n == 0 || n == 1) {
        printf("The Nth term in the sequence is 0\n");
    }

    //value for input 2 (third term)
    else if (n == 2) {
        printf("The Nth term in the sequence is 1\n");

    }

    //Use equation Tn = Tn-1 + Tn-2 + Tn-3
    else {
        U64 d;
        for (U64 i = 0; i < n - 2; i++) {
            d = a + b + c;
            a = b;
            b = c;
            c = d;
        }
        printf("The Nth term in the sequence is %llu\n",d);
    }

    return 0;

}