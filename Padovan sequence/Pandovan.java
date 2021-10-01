// Java program to find n'th term
// in Padovan Sequence using
// Dynamic Programming
import java.io.*;

class GFG {
	
	/* Function to calculate
	padovan number P(n) */
	static int pad(int n)
	{
	int []padv=new int[n]; //create array to store padovan values
	padv[0]=padv[1]=padv[2]=1;
		for (int i = 3; i <= n; i++) {
		padv[i]=padv[i-2]+padv[i-3];
		}
		return padv[n-1];

		
	}

	/* Driver Program */
	public static void main(String args[])
	{
		int n = 12;
		System.out.println(pad(n));
	}
}

/*This code is contributed by Kanjam Bhat Lidhoo.*/
