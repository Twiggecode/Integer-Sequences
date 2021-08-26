// An Optimized Solution to check Abundant Number
// in JAVA
import java.io.*;
import java.math.*;
import java.util.*;
 
// Function to calculate sum of divisors
class Main{
    static int getSum(int n)
    {
        int sum = 0;
   
       // Note that this loop runs till square
       // root of n
        for (int i=1; i<=(Math.sqrt(n)); i++)
        {
            if (n%i==0)
            {
             // If divisors are equal,take only
             // one of them
                if (n/i == i)
                   sum = sum + i;
   
                else // Otherwise take both
                {
                   sum = sum + i;
                   sum = sum + (n / i);
                }
            }
        }
   
        // calculate sum of all proper divisors
       // only
        sum = sum - n;
        return sum;
    }
   
    // Function to check Abundant Number
    static boolean checkAbundant(int n)
    {
      // Return true if sum of divisors is
      // greater than n.
      return (getSum(n) > n);
    }
   
    /* Driver program to test above function */
    public static void main(String args[])throws
                                   IOException
    {
      int n ;
      Scanner sc = new Scanner(System.in);
      // enter the upper limit for finding the abundant numbers 
      n = sc.nextInt();
      for (int i =0 ; i <=n; i++){
        // check if n is an abundant number or not 
          if (checkAbundant(i))
            System.out.println(i);
      }
    }
}

  
