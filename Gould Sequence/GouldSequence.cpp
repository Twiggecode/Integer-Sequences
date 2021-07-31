#include<iostream>
using namespace std;

int main()
{
    int n,inp,count=0;
    cout<<"Enter the nth value: ";
    cin>>n;
    inp=n;
    while(inp)
    {
        count+=inp&1;
        inp>>=1;
    }
    cout<<n<<"th row in the pascal triangle has "<<(1<<count)<<" odd numbers!";
    return 0;
}