#include <iostream>
#include <math.h>
using namespace std;
 
long int cullen_number(long int n){
    return n * pow(2, n) + 1;
}

int main(){
	long int number;

	while(true){
		cout << "Enter a number: ";
		cin >> number;

		if(number > -1){
			break;
		}
		else{
			cout << "Natural number expected!\n";
		}
	}

	cout<<cullen_number(number);
}