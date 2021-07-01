import java.util.InputMismatchException;
import java.util.Scanner;

public class Fermat {

	// This class returns the nth element of the Fermat numbers where n is a positive integer (or zero) input by the user
	
	public static void main(String[] args) {
		System.out.println("The Nth element of the Fermat numbers is " + fermat());	
	}

	public static int userInput() {
		Scanner scanner = new Scanner(System.in);
		int n = -1;				
		// The loop is used to check if the number input by the user is a positive integer or zero
		while(true) {
			// Keeps track if exception was encountered
			boolean exception = false;
			try {
        		System.out.print("Enter a number: ");
        		// Prompt the user to enter a number
        		n = scanner.nextInt();	
        	} 
			// Catches an exception if the user input is not an integer
        	catch (InputMismatchException e) {
        			System.out.println("Invalid input. Please enter an integer input.\n");
        			// Discards the invalid token inputed to avoid an infinite loop
        			scanner.next();
        			// True if exception was encountered
        			exception = true;
        	}
        	if(n > -1) {
        		scanner.close();
        		return n;
        	}
        	// Else a negative integer was inputed
        	else if(exception == false) {
        		System.out.println("Invalid number. Please enter a positive number.\n");
        	}
		}
    }
	
	public static long fermat() {
		int n = userInput();
		// Calculate the Fermat numbers using Fn = 2^(2^n)  + 1	
		return Math.round(Math.pow(2,Math.pow(2,n)) +1);		
	}
}
