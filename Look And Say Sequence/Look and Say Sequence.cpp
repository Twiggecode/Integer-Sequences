#include <bits/stdc++.h>
using namespace std;
 
// generator function returns int string from prev int
// string e.g. -> it will return '1211' for '21' ( One 2's
// and One 1)
string generator(string str)
{
    string ans = "";
 
    unordered_map<char, int>
        tempCount; // It is used to count integer sequence
 
    for (int i = 0; i < str.length() + 1; i++) {
        // when current char is different from prev one we
        // clear the map and update the ans
        if (tempCount.find(str[i]) == tempCount.end()
            && i > 0) {
            auto prev = tempCount.find(str[i - 1]);
            ans += to_string(prev->second) + prev->first;
            tempCount.clear();
        }
        // when current char is same as prev one we increase
        // it's count value
        tempCount[str[i]]++;
    }
 
    return ans;
}
 
string countnndSay(int n)
{
    string res = "1"; // res variable keep tracks of string
                      // from 1 to n-1
 
    // For loop iterates for n-1 time and generate strings
    // in sequence "1" -> "11" -> "21" -> "1211"
    for (int i = 1; i < n; i++) {
        res = generator(res);
    }
 
    return res;
}
 
int main()
{
 
    int N ;
    cin >> N;
    cout << countnndSay(N) << endl;
    return 0;
}
