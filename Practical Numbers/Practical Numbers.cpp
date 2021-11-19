#include <bits/stdc++.h>
using namespace std;
 
// Returns true if there is a subset of set[]
// with sun equal to given sum
bool isSubsetSum(vector<int>& set, int n, int sum)
{
    // The value of subset[i][j] will be true if
    // there is a subset of set[0..j-1] with sum
    // equal to i
    bool subset[n + 1][sum + 1];
 
    // If sum is 0, then answer is true
    for (int i = 0; i <= n; i++)
        subset[i][0] = true;
 
    // If sum is not 0 and set is empty,
    // then answer is false
    for (int i = 1; i <= sum; i++)
        subset[0][i] = false;
 
    // Fill the subset table in bottom up manner
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= sum; j++) {
            if (j < set[i - 1])
                subset[i][j] = subset[i - 1][j];
            if (j >= set[i - 1])
                subset[i][j] = subset[i - 1][j]
                               || subset[i - 1][j - set[i - 1]];
        }
    }
    return subset[n][sum];
}
 
// Function to store divisors of N
// in a vector
void storeDivisors(int n, vector<int>& div)
{
    // Find all divisors which divides 'num'
    for (int i = 1; i <= sqrt(n); i++) {
 
        // if 'i' is divisor of 'n'
        if (n % i == 0) {
 
            // if both divisors are same
            // then store it once else store
            // both divisors
            if (i == (n / i))
                div.push_back(i);
            else {
                div.push_back(i);
                div.push_back(n / i);
            }
        }
    }
}
 
// Returns true if num is Practical
bool isPractical(int N)
{
    // vector to store all
    // divisors of N
    vector<int> div;
    storeDivisors(N, div);
    // to check all numbers from 1 to < N
    for (int i = 1; i < N; i++) {
        if (!isSubsetSum(div, div.size(), i))
            return false;
    }
    return true;
}
 
// Driver code
int main()
{
    int N ;
    cin >> N;
    for(int i =0 ;i < N ; i++){
        if (isPractical(i))
            cout << i << " ";
    }
    return 0;
}
