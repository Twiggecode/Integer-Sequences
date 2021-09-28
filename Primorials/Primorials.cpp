#include<bits/stdc++.h>
using namespace std;
const int MAX = 1000000;
vector <int> primeNumbers;
void findPrimes() {
   bool marked[MAX/2 + 1] = {0};
   for (int i = 1; i <= (sqrt(MAX)-1)/2 ; i++)
      for (int j = (i*(i+1))<<1 ; j <= MAX/2 ; j += 2*i +1)
         marked[j] = true;
   primeNumbers.push_back(2);
   for (int i=1; i<=MAX/2; i++)
      if (marked[i] == false)
         primeNumbers.push_back(2*i + 1);
}
int findPrimorial(int n) {
   findPrimes();
   int result = 1;
   for (int i=0; i<n; i++)
   result = result * primeNumbers[i];
   return result;
}
int main() {
   int N ;
   cin >> N;
   cout<<"Primorial(P#) of first "<<N<<" prime numbers is "<<findPrimorial(N)<<endl;
   return 0;
}
