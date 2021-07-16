//Program in cpp to compute Narayan number of sequence 1 1 1 2 3 4 6 9 13 19 .....
#include<bits/stdc++.h>
using namespace std;

int main(){
	int num;
	cin>>num;
	vector<int> N(num+1);
	N[0]=N[1]=N[2]=1;
	if(num<=2){
		cout<<N[num];
	}
	else{
	  for(int i=3;i<=num;i++){
	  	N[i]=N[i-1]+N[i-3];
	  }
	   cout<<N[num];
	}
	return 0;
}
