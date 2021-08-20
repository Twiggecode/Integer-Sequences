// C++ program to print Farey Sequence of given order
#include <bits/stdc++.h>
using namespace std;
 
// class for x/y (a term in farey sequence
class Term {
public:
    int x, y;
 
    // Constructor to initialize x and y in x/y
    Term(int x, int y)
        : x(x), y(y)
    {
    }
};
 
// Comparison function for sorting
bool cmp(Term a, Term b)
{
    // Comparing two ratio
    return a.x * b.y < b.x * a.y;
}
 
// GCD of a and b
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}
 
// Function to print Farey sequence of order n
void farey(int n)
{
    // Create a vector to store terms of output
    vector<Term> v;
 
    // One by one find and store all terms except 0/1 and n/n
    // which are known
    for (int i = 1; i <= n; ++i) {
        for (int j = i + 1; j <= n; ++j)
 
            // Checking whether i and j are in lowest term
            if (gcd(i, j) == 1)
                v.push_back(Term(i, j));
    }
 
    // Sorting the term of sequence
    sort(v.begin(), v.end(), cmp);
 
    // Explicitly printing first term
    cout << "0/1 ";
 
    // Printing other terms
    for (int i = 0; i < v.size(); ++i)
        cout << v[i].x << "/" << v[i].y << " ";
 
    // explicitely printing last term
    cout << "1/1";
}
 
// Driver program
int main()
{
    int n;
    cin >> n;
    cout << "Farey Sequence of order " << n << " is\n";
    farey(n);
    return 0;
}
