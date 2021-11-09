#include<bits/stdc++.h>
using namespace std;
 
void GenAllPrim(int n1, bool prarr1[])
{
    for (int i=0; i<=n1; i++)
        prarr1[i] = true;
 
    for (int p=2; p*p<=n1; p++)
    {
        if (prarr1[p] == true)
        {
            for (int i=p*2; i<=n1; i += p)
                prarr1[i] = false;
        }
    }
}
void chkMerPrime(int nm)
{
    bool prarr1[nm+1];
    GenAllPrim(nm,prarr1);
    for (int j=2; ((1<<j)-1) <= nm; j++)
    {
        long long num = (1<<j) - 1;
        if (prarr1[num])
            cout <<" "<< num << " ";
    }
}
int main()
{
    int n ;
	cout << "\n\n Generate Mersenne primes within a range of numbers:\n";
	cout << "--------------------------------------------------------\n";
	cout << " Input a upper limit [range from 1 to upper limit]: ";
    cin>>n;	
    cout << " Mersenne prime numbers are: "<<endl;
    chkMerPrime(n);
    cout<<endl<<endl;
}
