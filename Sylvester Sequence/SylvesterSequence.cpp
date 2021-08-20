//Sylvester Sequence  


//Example : 2 3 7 43 1807 3263443 ....

#include<bits/stdc++.h> 
using namespace std;
int MOD = 1e9 +7;

long long int Sylvester_number(int n){
	if(n==0){
		return 2;  
	}
	long long int ans=2,previous=1;
	for(int i=1; i<=n; i++){
		ans = ((previous % MOD)*(ans % MOD) + MOD) % MOD;
		previous=ans; 
		ans=(ans+1)%MOD; 
	}
	return ans; 
}

int main(){
	int x;
	cin>>x;
	cout<<Sylvester_number(x);
}