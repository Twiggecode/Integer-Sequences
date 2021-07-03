#include<bits/stdc++.h>
using namespace std;


int FastPowerOf2(int n){  // returns nth power of 2 using Bit Manipulation
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

int main(){
	int n;
	cout<<"Enter the power of 2 : ";
	cin >> n;
	cout<<n<<"to the Power of 2 is : "<<FastPowerOf2(n);
	return 0;
}

