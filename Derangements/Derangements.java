import java.io.*;
import java.util.*;
class Main {
   
    // Function to count derangements 
    static int countDer(int n) {
        // Base case
          if(n == 1 || n == 2) {
            return n-1;
        }
       
        // Variable for storing prev values
        int a = 0;
          int b = 1;
       
        // manner using above recursive formula
        for (int i = 3; i <= n; ++i) {
            int cur = (i-1)*(a+b);
            a = b;
              b = cur;
        }
             
        // Return result for n
        return b;
    }
       
    // Driver Code
    public static void main (String[] args) 
    {
        int n ;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        System.out.println("Count of Dearrangements is " + 
                            countDer(n));
       
    }
   
  // Code contributed by skagnihotri
}
