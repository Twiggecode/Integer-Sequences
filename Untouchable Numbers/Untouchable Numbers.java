import java.util.*;
// Java program for the above approach
class Main{
 
// Function to calculate sum of
// all proper divisors of num
static int divSum(int num)
{
 
    // Final result of summation
    // of divisors
    int result = 0;
 
    // Find all divisors of num
    for(int i = 2; i <= Math.sqrt(num); i++)
    {
        
       // If 'i' is divisor of 'num'
       if (num % i == 0)
       {
            
           // If both divisors are same
           // then add it only once else
           // add both
           if (i == (num / i))
               result += i;
           else
               result += (i + num / i);
       }
    }
     
    // Add 1 to the result as
    // 1 is also a divisor
    return (result + 1);
}
 
// Function to check if N is a
// Untouchable Number
static boolean isUntouchable(int n)
{
    for(int i = 1; i <= 2 * n; i++)
    {
       if (divSum(i) == n)
           return false;
    }
    return true;
}
 
// Driver code
public static void main(String[] args)
{
 
    // Given Number N
    int n;
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    // Function Call
    for (int i =0 ; i<=n; i++)
        if (isUntouchable(i))
            System.out.print(i+" ");
}
}
