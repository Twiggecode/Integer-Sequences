#include <iostream>
using namespace std;
 
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

	cout<<catalan_number(number);
}