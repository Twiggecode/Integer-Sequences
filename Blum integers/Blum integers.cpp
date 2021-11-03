#include <bits/stdc++.h>
using namespace std;
 
// Function to cheek if number is Blum Integer
bool isBlumInteger(int n)
{
    bool prime[n + 1];
    memset(prime, true, sizeof(prime));
 
    // to store prime numbers from 2 to n
    for (int i = 2; i * i <= n; i++) {
 
        // If prime[i] is not
        // changed, then it is a prime
        if (prime[i] == true) {
 
            // Update all multiples of p
            for (int j = i * 2; j <= n; j += i)
                prime[j] = false;
        }
    }
 
    // to check if the given odd integer
    // is Blum Integer or not
    for (int i = 2; i <= n; i++) {
        if (prime[i]) {
 
            // checking the factors
            // are of 4t+3 form or not
            if ((n % i == 0) && ((i - 3) % 4) == 0) {
                int q = n / i;
                return (q != i && prime[q] &&
                           (q - 3) % 4 == 0);
            }
        }
    }
 
    return false;
}
 
// driver code
int main()
{
    // give odd integer greater than 20
    int n;
    cin >> n;
    // enter n for the range until which you want to print BlumIntegers
    for (int i =0 ; i < n ; i++){
        if (isBlumInteger(i))
            cout << i << " ";
    }
}
