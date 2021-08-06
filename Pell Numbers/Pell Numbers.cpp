// Pell Number Series using Recursion in C++
#include <bits/stdc++.h>
using namespace std;
 
// calculate nth pell number
int pell(int n)
{
    if (n <= 2)
        return n;
    return 2 * pell(n - 1) + pell(n - 2);
}
 
// Driver Code
int main()
{
    int n;
    cin >>n;
    cout << " " << pell(n);
    return 0;
}
