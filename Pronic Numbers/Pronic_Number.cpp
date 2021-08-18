#include <iostream>
using namespace std;
int main ()
{
  int i, inp, num = 1, c = 0, latest = 0;
  cout<<"Enter the Nth Value: ";
  cin>>inp;
  while (c != inp)
    {
    int flag=0;
     for(i=0;i<=num;i++)
   {
       if(i*(i+1)==num)
       {
           flag=1;
           break;
       }
   }

   if(flag==1)
   {
          c++;
          latest=num;
    }
      num = num + 1;
    }
  cout<<"The "<<inp<<"th Pronic Number is: "<<latest<<"\n";
  return 0;
}