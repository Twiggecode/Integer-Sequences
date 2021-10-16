#include <bits/stdc++.h>
using namespace std;
 
// Function to count the number
// of divisors of the N
int divCount(int n)
{
    // sieve method for prime calculation
    bool hash[n + 1];
    memset(hash, true, sizeof(hash));
    for (int p = 2; p * p < n; p++)
        if (hash[p] == true)
            for (int i = p * 2; i < n; i += p)
                hash[i] = false;
 
    // Traversing through
    // all prime numbers
    int total = 1;
    for (int p = 2; p <= n; p++) {
        if (hash[p]) {
 
            // calculate number of divisor
            // with formula total div =
            // (p1+1) * (p2+1) *.....* (pn+1)
            // where n = (a1^p1)*(a2^p2)....
            // *(an^pn) ai being prime divisor
            // for n and pi are their respective
            // power in factorization
            int count = 0;
            if (n % p == 0) {
                while (n % p == 0) {
                    n = n / p;
                    count++;
                }
                total = total * (count + 1);
            }
        }
    }
    return total;
}
 
// Function to check if a number
// is a highly composite number
bool isHighlyCompositeNumber(int N)
{
    // count number of factors of N
    int NdivCount = divCount(N);
 
    // loop to count number of factors of
    // every number less than N
    for (int i = 1; i < N; i++) {
        int idivCount = divCount(i);
 
        // If any number less than N has
        // more factors than N,
        // then return false
        if (idivCount >= NdivCount)
            return false;
    }
 
    return true;
}
 
// Driver code
int main()
{
    // Given Number N
    int N;
    cin >> N;
    
 
    // Function Call
    for ( int i =0 ; i < N ; i++){
    if (isHighlyCompositeNumber(i))
        cout << i << " " ;
    }
    return 0;
}
