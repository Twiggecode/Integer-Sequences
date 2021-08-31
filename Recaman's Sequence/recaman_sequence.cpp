/*

    C++ Program to find the nth number of Recaman Sequence

*/

#include <bits/stdc++.h>
using namespace std;

vector<int> findRecamanSequence(int n) {
    vector<int> recamanSequence;
    recamanSequence.push_back(0);
    
    map<int, bool> isExist;
    isExist[0] = true;

    for (int i = 1; i <= n; i++) {
        int prev = recamanSequence[i - 1];

        if (prev - i > 0 && !isExist[prev - i]) {
            recamanSequence.push_back(prev - i);
            isExist[prev - i] = true;
        } else {
            recamanSequence.push_back(prev + i);
            isExist[prev + i] = true;
        }
    }

    return recamanSequence;
}

// Main Function
int main()
{
    int n;

    cout<< "Enter a number: ";
    cin>> n;

    vector<int> recamanSequence = findRecamanSequence(n);
    cout<< "The " << n << "th number of recaman sequence is: " << recamanSequence[n] << "\n";

    return 0;
}
