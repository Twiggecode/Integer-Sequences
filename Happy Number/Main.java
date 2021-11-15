/******************************************************************************
Happy Number code in java
*******************************************************************************/
import java.util.*;
public class Main
{
    static int summer(int n)  // Gets sum of squares of the digits
    {
        int i,j,s=0;
        
        for(i=n;i!=0;i=i/10)
        {
            j=i%10;
            s+=(j*j);
        }
        
        return s;
    }
	public static void main(String[] args) {
		
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter Number");
		
		int a=sc.nextInt();   // Scanner class to take input
		
		int n=a;   // backup of number
		
		while(true) // Loop for checking Happy Number
		{
		    if(summer(n) == 1)
		    {   System.out.println("True");  break;  }
		    
            n = summer(n);
            
            if (n < 10)
            {   System.out.println("False"); break;  }
		
		    
		}
		
	}
}
