/*################################
## Look and Say Sequence      ##
################################

#Idea : Every current term is dependent on previous term
#Example : 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
#1 is read off as "one 1" or 11.
#11 is read off as "two 1s" or 21.
#21 is read off as "one 2, then one 1" or 1211.
#111221 is read off as "three 1s, two 2s, then one 1" or 312211.*/
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

string seq(int n){
        if(n == 1){
                return "1";
        }
        if(n == 2){
                return "11";
        }
        string s = "11";
        for (int i=3;i<=n;i++){
                s += "$";
                int l = s.length();
                int count = 1;
                string tmp = "";
                for (int j=1;j<l;j++){
                        if(s[j] != s[j-1]){
                                tmp += to_string(count + 0);
                                tmp += s[j-1];
                                count = 1;
                        }
                        else{
                                count += 1;
                        }
                }
                s = tmp;
        }
        return s;
}

int main(){
    cout << "Enter the nth value to find: ";
    int n;
    cin>>n;
    cout<<n<<"th value in Look and Say Sequence is: "<<seq(n);
    return 0;
}