#include<bits/stdc++.h>
#define long long ll
using namespace std;

int main(){
	int n;
	cout<<"Enter the power of 2 : ";
	cin >> n;
	//we can directly use the left shift operator to calculate 2^n.
	//This is a bitwise operator.
	//we can ll to convert to long long.
	cout<<n<<"to the Power of 2 is : "<<(1ll<<n);
	return 0;
}

