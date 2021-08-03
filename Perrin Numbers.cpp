
//  perrin number using Recursion
#include <bits/stdc++.h>
using namespace std;
 
int per(int n)
{
    if (n == 0)
        return 3;
    if (n == 1)
        return 0;
    if (n == 2)
        return 2;
    return per(n - 2) + per(n - 3);
}
 
// Driver code
int main()
{
    int n;
    cin >> n;
    for( int i = 0; i<=n;i++)
    {
    cout << per(i)<<" ";
    }
    return 0;
}
 
