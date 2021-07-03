#include<bits/stdc++.h>
using namespace std;

// example of Fibonacci sequence ------ 0, 1, 1, 2, 3, 5, 8, 13....
// 1st and 2nd term = 0 , 1 respectively and proceeding terms are sum of previous two terms 

int Fibonacci(int i){   // Fibonacci function expects index of the sequence
						// and returns the term present at the index
	if(i == 0 or i == 1){
		return i;
	}
	else{
		return Fibonacci(i-1) + Fibonacci(i-2) ;
	}
}

int main(){
	int n; // n is the expected user input
	cout<<"Enter the required index of Fibonacci sequence : ";
	cin >> n ;
	cout<<"The Term at required index of Fibonacci sequence is : ";
	cout<<Fibonacci(n);
return 0;
}


