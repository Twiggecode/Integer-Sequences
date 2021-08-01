// Cpp code to print nth
// Ulam number
 
#include <bits/stdc++.h>
using namespace std;
 
#define MAX 10000
 
// Array to store Ulam Number
vector<int> arr;
 
// function to compute ulam Number
void ulam()
{
 
    // Set to search specific Ulam number efficiently
    unordered_set<int> s;
 
    // push First 2 two term of the sequence
    // in the array and set
    // for further calculation
 
    arr.push_back(1);
    s.insert(1);
 
    arr.push_back(2);
    s.insert(2);
 
    // loop to generate Ulam number
    for (int i = 3; i < MAX; i++) {
 
        int count = 0;
 
        // traverse the array and check if
        // i can be represented as sum of
        // two distinct element of the array
 
        for (int j = 0; j < arr.size(); j++) {
 
            // Check if i-arr[j] exist in the array or not using set
            // If yes, Then i can be represented as
            // sum of arr[j] + (i- arr[j])
 
            if (s.find(i - arr[j]) != s.end() && arr[j] != (i - arr[j]))
                count++;
 
            // if Count is greater than 2
            // break the loop
            if (count > 2)
                break;
        }
 
        // If count is 2 that means
        // i can be represented as sum of
        // two distinct terms of the sequence
 
        if (count == 2) {
            // i is ulam number
            arr.push_back(i);
            s.insert(i);
        }
    }
}
 
// Driver code
int main()
{
    // pre compute Ulam Number sequence
    ulam();
 
    int n;
    cin>>n;
 
    // print nth Ulam number
    for (int i = 0 ; i<n ;i++) 
        cout<<arr[i]<<endl;
    return 0;
}
