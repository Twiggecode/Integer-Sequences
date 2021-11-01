#include <iostream>
using namespace std;
 
// utility function to find gcd of two numbers
int gcd(int a, int b)
{
    if (a < b)
        return gcd(b, a);
    if (a % b == 0)
        return b;
    return gcd(b, a % b);
}
 
// utility function to find pow(x, y) under
// given modulo mod
int power(int x, int y, int mod)
{
    if (y == 0)
        return 1;
    int temp = power(x, y / 2, mod) % mod;
    temp = (temp * temp) % mod;
    if (y % 2 == 1)
        temp = (temp * x) % mod;
    return temp;
}
 
// This function receives an integer n and
// finds if it's a Carmichael number
bool isCarmichaelNumber(int n)
{
    for (int b = 2; b < n; b++) {
        // If "b" is relatively prime to n
        if (gcd(b, n) == 1)
 
            // And pow(b, n-1)%n is not 1,
            // return false.
            if (power(b, n - 1, n) != 1)
                return false;
    }
    return true;
}
 
// Driver function
int main()
{   int n;
    string ans;
    cin >> n;
    ans= isCarmichaelNumber(n)?"True":"False";
    cout << ans<<endl;
    return 0;
}
