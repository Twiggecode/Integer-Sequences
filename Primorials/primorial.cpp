/*

    C++ Program to find the product of the first n primes as nth primorial number.

*/

#include <bits/stdc++.h>
using namespace std;

#define MAX 1000005

bool marked[MAX];
vector<int> primes;

void sieve()
{
    marked[0] = marked[1] = true;

    for(int i = 2; i * i <= MAX - 1; i++){
        if(marked[i] == false){
            for(int j = i*i; j <= MAX - 1; j += i){
                marked[j]=true;
            }
        }
    }

    for (int i = 0; i < MAX; i++){
        if(!marked[i]){
            primes.push_back(i);
        }
    }
}

long long int findPrimorial(int n) {
    long long int result = 1;

    for (int i = 0; i < n; i++) {
        result *= primes[i];
    }

    return result;
}

// Main Function
int main()
{
    int n;
    sieve();
    
    cout<< "Enter a number: ";
    cin>> n;
    cout<< "The " << n << "th number's primorial value is: " << findPrimorial(n) << "\n";

    return 0;
}
