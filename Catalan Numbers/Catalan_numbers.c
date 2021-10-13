#include <stdio.h>
//function to find kth catalan number
long int catalan_number(long int n){

    if (n <= 1){
        return 1;
	}

    long int result = 0;

    for (int i = 0; i < n; i++){
        result += catalan_number(i) * catalan_number(n - i - 1);
	}
 
    return result;
}

int main(){
	long int number;
 //check for invalid input
	while(1){
		printf("Enter a number: ");
		scanf("%li",&number);

		if(number > -1){
			break;
		}
		else{
			printf("Natural number expected!\n");
		}
	}

    printf("%li",catalan_number(number));
}
