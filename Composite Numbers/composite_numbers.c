#include <stdio.h>

int isPrime(int num){
    if (num <= 3)
    {
        return num > 1;
    }
    if ((num % 2 == 0) || (num % 3 == 0))
    {
        return 0;
    }
    int i = 5;
    while (i * i < num)
    {
        if ((num % i == 0) || (num % (i + 2) == 0))
        {
            return 0;
        }
        i = i + 6;
    }
    return 1;
}

int main(){
    int input;
    printf("Enter n: ");
    scanf("%d", &input);
    int count = -1;
    int curr = 2;
    while(count < input)
    {
        curr++;
        if (!isPrime(curr))
        {
            count++;
        }
    }
    printf("%d\n", curr);
}
