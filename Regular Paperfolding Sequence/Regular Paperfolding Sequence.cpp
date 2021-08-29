// CPP code to find nth term
// of the Dragon Curve Sequence
#include <bits/stdc++.h>
using namespace std;
  
// function to generate the nth term
string Dragon_Curve_Sequence(int n) 
{
    // first term
    string s = "1"; 
  
    // generating each term of the sequence
    for (int i = 2; i <= n; i++) 
    {
        string temp = "1";
        char prev = '1', zero = '0', one = '1';
  
        // loop to generate the ith term
        for (int j = 0; j < s.length(); j++) 
        {
            // add character from the 
            // original string
            temp += s[j];
  
            // add alternate 0 and 1 in between
            if (prev == '0') 
            {
                // if previous added term
                // was '0' then add '1'
                temp += one;
  
                // now current term becomes
                // previous term
                prev = one;
            }
            else 
            {
                // if previous added term
                // was '1', then add '0'
                temp += zero;
  
                // now current term becomes
                // previous term
                prev = zero;
            }
        }
          
        // s becomes the ith term of the sequence
        s = temp;
    }
    return s;
}
  
// Driver program
int main()
{
    // Taking input
    int n ;
    cin >> n;
  
    // generate nth term of dragon curve sequence
    string s = Dragon_Curve_Sequence(n);
      
    // Printing output
    cout << s << "\n";
}
