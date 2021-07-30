#include <bits/stdc++.h>
/*
In pandovan sequence every pandovan number is a sum of previous two terms in the following way -:
P(n) = P( n - 2) + P( n - 3 ) .
here 'P(n)' is pandovan value of number 'n' , n >= 0 , P(0) = P(1) = P(2) = 1.
it is similar to fibonacci sequence in it's recursive manner .
for eg -: 1,1,1,2,2,3,4,5,7,9..... for indices 0,1,2.... respectively.
*/
using namespace std ;

int pad(int n)
{
    
    int pPrevPrev = 1, pPrev = 1, pCurr = 1, pNext = 1;
 
    for (int i=3; i<n; i++)
    {
        pNext = pPrevPrev + pPrev;
        pPrevPrev = pPrev;
        pPrev = pCurr;
        pCurr = pNext;
    }
 
    return pCurr;
}
int main()
{  int i , n ;                                                            
   cout << "Enter the index for respective pandovan number: " << endl ;
   cin >> n;                                                                                     
   i = pad(n ) ;                                                    
   cout << "The pandovan number for given index is: " << endl ;         
   cout << i ;
   return 0 ;
}


