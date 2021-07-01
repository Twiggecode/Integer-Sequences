import java.util.Scanner;

public class Fibonacci {

	public static void main(String[] args) {
		System.out.println("Enter a number:");
		Scanner in = new Scanner(System.in);
		int result = fib(in.nextInt()); // first solution in use -> Main Solution
		System.out.println(result);
		in.close();

	}
	
	/* Main Solution */
	static int fib(int n) {
		if (n < 2) {
			return n;
		}
		int a = 0;
		int b = 1;
		
		for (int i = 2; i <= n; i++) {
			int temp = a + b;
			a = b;
			b = temp;
		}
		return b;
	}
	
	
	
	
	/*  Recursive Solution */
	static int fib2(int n) {
		if (n == 0)
			return 0;
		if (n == 1)
			return 1;
		return fib(n-1) + fib(n-2);
	}
	
	/*	Dinamic Programming
	 *  If needed all the elements in the sequence -> return the array
	 */
	static int fib3(int n) {
		if (n < 2) {
			return n;
		}
		int[] fibN = new int[n+1];
		
		fibN[0] = 0;
		fibN[1] = 1;
		
		for (int i = 2; i <= n; i++) {
			fibN[i] = fibN[i-1] + fibN[i-2];
		}
		return fibN[n];
		
	}
}
