// An Optimized Solution to check Abundant Number
#include <bits/stdc++.h>
using namespace std;
 
// Function to calculate sum of divisors
int getSum(int n)
{
    int sum = 0;
 
    // Note that this loop runs till square root
    // of n
    for (int i=1; i<=sqrt(n); i++)
    {
        if (n%i==0)
        {
            // If divisors are equal,take only one
            // of them
            if (n/i == i)
                sum = sum + i;
 
            else // Otherwise take both
            {
                sum = sum + i;
                sum = sum + (n / i);
            }
        }
    }
 
    // calculate sum of all proper divisors only
    sum = sum - n;
    return sum;
}
 
// Function to check Abundant Number
bool checkAbundant(int n)
{
    // Return true if sum of divisors is greater
    // than n.
    return (getSum(n) > n);
}
 
/* Driver program to test above function */
int main()
{   int n,count=-1,i=12 ; cin >> n;
    while (count!=n)
    {
       if (checkAbundant(i)){
            
            count++;
       }
       i++;
    }
       
   cout<<i-1;

    return 0;
}
