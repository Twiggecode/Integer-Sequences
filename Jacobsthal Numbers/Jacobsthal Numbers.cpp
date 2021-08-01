// A simple C++ recursive solution to find
// Jacobsthal sequence
#include <bits/stdc++.h>
using namespace std;
 
// Return Jacobsthal number.
int Jacobsthal(int n)
{
    // base case
    if (n == 0)
        return 0;
 
    // base case
    if (n == 1)
        return 1;
 
    // recursive step.
    return Jacobsthal(n - 1) + 2 * Jacobsthal(n - 2);
}
// Driven Program
int main()
{
    int n;
    cin >> n;
    cout << "Jacobsthal number sequence: ";
    for ( int i =1; i <=n; i++){
    cout << Jacobsthal(i) << endl;
    return 0;
}
