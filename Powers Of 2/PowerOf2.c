#include <stdio.h>

typedef unsigned long long int U64;

//Prints the nth power of 2 using Bit Manipulation
U64 FastPowerOf2(U64 n){  
	int x =2;
	int res =1;
	while(n>0){
		if(n&1 != 0){
			res = res * x;
		}
		x *= x;
		n = n>>1;
	}
	return res;
}

int main(void)
{
    U64 n;
    printf("Please enter the power of 2: ");
    scanf("%llu",&n);
    printf("%llu to the power of 2 is: %llu",n,FastPowerOf2(n));
    return 0;
}
