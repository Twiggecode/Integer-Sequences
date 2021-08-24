// CPP program to find zigzag sequence
#include <bits/stdc++.h>
using namespace std;
 
// Function to print first n zigzag numbers
void ZigZag(int n)
{
    // To store factorial and n'th zig zag number
    long long fact[n + 1], zig[n + 1] = { 0 };
 
    // Initialize factorial upto n
    fact[0] = 1;
    for (int i = 1; i <= n; i++)
        fact[i] = fact[i - 1] * i;
 
    // Set first two zig zag numbers
    zig[0] = 1;
    zig[1] = 1;
 

    // Print first two zig zag number
    cout << zig[0] << " " << zig[1] << " ";
 
    // Print the rest zig zag numbers
    for (int i = 2; i < n; i++)
    {
        long long sum = 0;
 
        for (int k = 0; k <= i - 1; k++)
        {
            // Binomial(n, k)*a(k)*a(n-k)
            sum += (fact[i - 1]/(fact[i - 1 - k]*fact[k]))
                                 *zig[k] * zig[i - 1 - k];
        }
         
        // Store the value
        zig[i] = sum / 2;
 
        // Print the number
        cout << sum / 2 << " ";
    }
}
 
// Driver code
int main()
{
    int n;
    cin >> n;
     
    // Function call
    for ( int i =0; i <n ;i++)
    ZigZag(n);
 
    return 0;
}
