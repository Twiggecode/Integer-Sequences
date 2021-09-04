// C++ program for the above approach
#include <bits/stdc++.h>
using namespace std;
 
// Function to calculate sum of
// all proper divisors of num
int divSum(int num)
{
    // Final result of summation
    // of divisors
    int result = 0;
 
    // Find all divisors of num
    for (int i = 2; i <= sqrt(num); i++) {
 
        // If 'i' is divisor of 'num'
        if (num % i == 0) {
 
            // If both divisors are same
            // then add it only once else
            // add both
            if (i == (num / i))
                result += i;
            else
                result += (i + num / i);
        }
    }
 
    // Add 1 to the result as
    // 1 is also a divisor
    return (result + 1);
}
 
// Function to check if N is a
// Untouchable Number
bool isUntouchable(int n)
{
    for (int i = 1; i <= 2 * n; i++) {
        if (divSum(i) == n)
            return false;
    }
    return true;
}
 
// Driver Code
int main()
{
    // Given Number N
    int N;
    cin >> N;
    for (int i =0; i < N; i++){
    // Function Call
      if (isUntouchable(n))
        cout << i << end;
    }
}
