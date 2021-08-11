#include <iostream>
using namespace std;

/* Lazy caterer's sequence 
describes the maximum number of pieces a circular pizza
can be divided into with an increasing number of cuts,n.
recursive formula is f(n) = f(n-1) + n*/


int main(){
    int n;
    cout<<"Enter a number: ";
    cin>>n;
    cout<<"A circular pizza can be divided into "<<(n*(n+1))/2 +1<<" pieces with "<<n<<" cuts!";
    return 0;
}