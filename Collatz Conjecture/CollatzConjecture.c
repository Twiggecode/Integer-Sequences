#include <stdio.h>

int* collatz(int *n){
    if(*n % 2 == 0){
        *n /= 2; 
    }
    else if(*n % 2 == 1){
        *n = 3 * (*n) + 1; 
    }
    return n; 
}

int main(void){
    int num = 0, counter = 1;
    printf("Enter a number greater than 0: ");
    scanf("%d", &num);
    
    while(num != 1){
        counter++;
        collatz(&num);
        printf("This is collatz conjecture at step %d = %d \n", counter, num);
    }
    return 0; 
}
