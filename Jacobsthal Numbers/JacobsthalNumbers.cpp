#include<iostream>
using namespace std;
/*Jacobsthal Numbers

#Forumula: J(n) = J(n-1)+2*J(n-2)
#Example:  0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, 10923, 21845, 43691, ……*/

int jacob(int n){
    n=n-1; // As first term is 0
    int dp[n+1]={0};
    dp[0]=0;
    dp[1]=1;
    for (int i=2; i<=n;i++){
        dp[i]=dp[i-1]+2*dp[i-2];
    }
    return dp[n];
}

int main(){
    int n;
    cout<<"Enter a number: ";
    cin>>n;
    cout<<"The "<<n<<"th value of Jacobsthal Number is: "<<jacob(n);
    return 0;
}