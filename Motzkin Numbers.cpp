// CPP Program to find Nth Motzkin Number.
#include <bits/stdc++.h>
using namespace std;
   
// Return the nth Motzkin Number.
int motzkin(int n)
{
    // Base Case
    if (n == 0 || n == 1)
        return 1;
   
    // Recursive step
    return ((2 * n + 1) * motzkin(n - 1) +
            (3 * n - 3) * motzkin(n - 2)) / (n + 2);
}
   
// Driven Program
int main()
{
    int n ;
    cin >>n;
    cout << motzkin(n) << endl;
    return 0;
}
