#include <bits/stdc++.h>
using namespace std;
/**
 * Alcuin Sequence
 * Formula: a(n) = round(n^2/12) – floor(n/4)*floor((n+2)/4)
 * Example: 0, 0, 0, 1, 0, 1, 1, 2, 1, 3, 2, 4, 3, 5, 4, 7 ...
 */

// Algorithm for calculating Alcuin numbers
int Alcuin(int n)
{
    double _n = n, val;
 
    val = round((_n * _n) / 12)
          - floor(_n / 4)
                * floor((_n + 2) / 4);
 
    return val;
}
 
// Main driver
int main()
{
    int n;
    cout<< "Enter the nth value to find: ";
    cin>> n;
    cout<< "The term at the required index of the Alcuin Sequence is ";
    cout<<Alcuin(n-1);
    return 0;
}