// CPP program to find N terms of the sequence
#include <bits/stdc++.h>
using namespace std;
 
// Stores the Wedderburn Etherington numbers
map<int, int> store;
 
// Function to return the nth
// Wedderburn Etherington numbers
int Wedderburn(int n)
{
    // Base case
    if (n <= 2)
        return store[n];
 
    // If n is even n = 2x
    else if (n % 2 == 0)
    {
        // get x
        int x = n / 2, ans = 0;
 
        // a(2x) = a(1)a(2x-1) + a(2)a(2x-2) + ... +
        // a(x-1)a(x+1)
        for (int i = 1; i < x; i++) {
            ans += store[i] * store[n - i];
        }
 
        // a(x)(a(x)+1)/2
        ans += (store[x] * (store[x] + 1)) / 2;
 
        // Store the ans
        store[n] = ans;
         
        // Return the required answer
        return ans;
    }
     
    else
    {
        // If n is odd
        int x = (n + 1) / 2, ans = 0;
 
        // a(2x-1) = a(1)a(2x-2) + a(2)a(2x-3) + ... +
        // a(x-1)a(x),
        for (int i = 1; i < x; i++) {
            ans += store[i] * store[n - i];
        }
 
        // Store the ans
        store[n] = ans;
         
        // Return the required answer
        return ans;
    }
}
 
 
// Function to print first N
// Wedderburn Etherington numbers
void Wedderburn_Etherington(int n)
{
    // Store first 3 numbers
    store[0] = 0;
    store[1] = 1;
    store[2] = 1;
     
    // Print N terms
    for (int i = 0; i < n; i++)
    {
        cout << Wedderburn(i);
        if(i!=n-1)
            cout << ", ";
    }
}
 
// Driver code
int main()
{
    int n;
  
    cin >> n;
 
    // function call
    Wedderburn_Etherington(n);
 
    return 0;
}
