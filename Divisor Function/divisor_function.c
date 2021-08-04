# include <stdio.h>
# include <stdlib.h>

long int div_func(long int n){
	if (n != 0){
		long int sum = n+1;
		long int i = 2;
		for( i = 2; i*i <= (n+1); i++){
			if ((n+1) % i == 0){
				sum = sum + i + (n+1) / i;
			}
		}
		return sum+1;
	}

	else{
		return 1;
	}
}

int isNum(char* p){
	long int i = 0;
	while(p[i]!='\0'){
		if (p[i] < 48 || p[i] > 57){
			return 0;
		}
		i++;
	}
	return 1;
}


int main()
{
	char x[1000000];
	long int n = 0;
	
	printf("enter the number: ");
	scanf("%s", x);
	if (isNum(&x) == 0){
		printf("Only whole numbers upto 1000000 are allowed!");
		return 0;
	}
	else{
		n = atoi(x);
	}
	if (n < 0)
	printf("n should be a whole number.");
	else
	printf("result: %ld", div_func(n));
	return 0;
}
