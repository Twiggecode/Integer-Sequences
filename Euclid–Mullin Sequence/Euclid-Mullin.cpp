#include<iostream>
using namespace std;

int smallPrimeFactor(int num){
	int p = 2;
	while((p * p) <= num){
		if(num % p == 0)
			return p;
		p += 1;
	}
	return num;
}


int seq(int n){
	int pdt = 1,ans=0;
	for(int i=0; i<n; i++){
		ans = smallPrimeFactor(pdt + 1);
		pdt *= ans;
	}
	return ans;
}

int main(){
	int i,n;
	cout<<"Enter the nth value to find : ";
	cin>>n;
	cout<<seq(n);
	return 0;
}
