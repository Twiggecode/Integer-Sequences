#include<bits/stdc++.h>
using namespace std;

int fib(int n)
{
    if (n <= 1) {
        return n;
    }
 
    return fib(n - 1) + fib(n - 2);
}
 
int main()
{
    int n;
    cout<<"which fibonacci number do you want?";
    cout<<endl;
    cin>>n;
 
    cout<< n<<"th fibonacci number in "<<fib(n);//since indexing starts from zero 
 
    return 0;
}