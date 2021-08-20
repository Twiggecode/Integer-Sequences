#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cout<<"which fibonacci number do you want?";
    cout<<endl;
    cin>>n;
    int p=0;
    int q=1;
    if(n==0)
    {
        cout<<0<<endl;
        exit;
    }
    if(n==1)
    {
        cout<<1<<endl;
        exit;
    }
    int z=n;
    n-=1;//since zero indexing
    int sum=0;
    while(n--)
    {
        sum=p+q;
        p=q;
        q=sum;
    }
    cout<<z<<"th fibonacci number is "<<sum<<endl;


}