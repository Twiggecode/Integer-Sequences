#include <bits/stdc++.h>
using namespace std;
 
// Utility function to check whether
// number is semiprime or not
int checkSemiprime(int num)
{
    int cnt = 0;
 
    for (int i = 2; cnt < 2 && i * i <= num; ++i)
        while (num % i == 0)
            num /= i, ++cnt; // Increment count
                             // of prime numbers
 
    // If number is greater than 1, add it to
    // the count variable as it indicates the
    // number remain is prime number
    if (num > 1)
        ++cnt;
 
    // Return '1' if count is equal to '2' else
    // return '0'
    return cnt == 2;
}
 
// Function to print 'True' or 'False'
// according to condition of semiprime
void semiprime(int n)
{
    if (checkSemiprime(n))
        cout << "True\n";
    else
        cout << "False\n";
}
 
// Driver code
int main()
{
    int n;
    cin>>n;
    semiprime(n);
    return 0;
}
