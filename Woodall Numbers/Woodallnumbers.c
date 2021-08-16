#include <stdio.h>
#include<math.h>
typedef unsigned long long int U64;

U64 Woodall(U64 n)
{
    return (n+1)*pow(2,n+1)-1;
    
}

int main(void)
{
    U64 n;
    printf("Please Enter N: ");
    scanf("%llu",&n);
    printf("The %llu th value of Woodall Number is: %llu",n,Woodall(n));
}
