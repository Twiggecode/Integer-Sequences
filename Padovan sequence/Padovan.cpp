#include <bits/stdc++.h>

/*
In pandovan sequence every pandovan number is a sum of previous two terms in the following way -:
P(n) = P( n - 2) + P( n - 3 ) .
here 'P(n)' is pandovan value of number 'n' , n >= 0 , P(0) = P(1) = P(2) = 1.
it is similar to fibonacci sequence in it's recursive manner .
for eg -: 1,1,1,2,2,3,4,5,7,9..... for indices 0,1,2.... respectively.
*/

using namespace std ;

int main()
{  int i , n ;                                                            //i acts as index.
   long long pandovan( long long ) ;
   cout << "Enter the index for respective pandovan number -: " << endl ;
   cin >> i ;                                                             //in this series the index provided                            
   n = pandovan( i ) ;                                                    //needs no change as the series's domain  
   cout << "The pandovan number for given index is -: " << endl ;         // itself begins from 0 .
   cout << n ;
   return 0 ;
}

long long pandovan( long long c )                    //the recursive function itself
{
  long long r = 0 ;
  if ( c >= 3 )
  {
    r = pandovan( c - 2 ) + pandovan( c - 3 ) ;
  }
  else 
  {
      if( c == 0 || c == 1 || c == 2 )
      {
          r = 1 ;
      }
      
  }
  return r ;
}
