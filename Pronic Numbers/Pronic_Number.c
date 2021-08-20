#include <stdio.h>
int main ()
{
  int i, inp, num = 1, c = 0, latest = 0;
  printf ("Enter the Nth value:");
  scanf ("%d", &inp);
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
  printf ("%dth Pronic number is %d\n", inp, latest);
  return 0;
}