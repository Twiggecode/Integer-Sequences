#include <iostream>
#include <math.h>

using namespace std;

long long carol_number(long long n){
	n++;
	return pow((pow(2, n) - 1), 2) - 2;
}

int main(){
	long long x;

	while(true){
		cout<<"Enter a number: ";
		cin>>x;
		if(x > -1)
			break;
		else
			cout<<"Natural number expected!\n";
	}

	cout<<carol_number(x);
}