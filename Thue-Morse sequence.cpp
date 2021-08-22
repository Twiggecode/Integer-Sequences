// CPP Program to find nth term of Thue-Morse sequence.
#include <bits/stdc++.h>
using namespace std;
 
// Return the complement of the binary string.
string complement(string s)
{
    string comps;
 
    // finding the complement of the string.
    for (int i = 0; i < s.length(); i++) {
 
        // if character is 0, append 1
        if (s.at(i) == '0')
            comps += '1';
 
        // if character is 1, append 0.
        else
            comps += '0';
    }
 
    return comps;
}
 
// Return the nth term of Thue-Morse sequence.
string nthTerm(int n)
{
    // Initialing the string to 0
    string s = "0";
 
    // Running the loop for n - 1 time.
    for (int i = 1; i < n; i++)
 
        // appending the complement of
        // the string to the string.
        s += complement(s);
     
 
    return s;
}
// Driven Program
int main()
{
    int n;
    cin >> n;
    cout << nthTerm(n) << endl;
    return 0;
}
