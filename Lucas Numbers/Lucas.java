import java.util.InputMismatchException;
import java.util.Scanner;

public class Lucas {

	// This class returns the nth element of the Lucas numbers where n is a positive integer (or zero) input by the user
	
	public static void main(String[] args) {
		System.out.println("The Nth element of the Lucas numbers is " + lucas());
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
	
	public static long lucas() {
		int n = userInput();
		switch(n) {
			case 0: {
				return 2;
			}
			case 1: {
				return 1;
			}
			case 2: {
				return 3;
			}
			// Defaults if n is greater than 2, and we use Ln = phi^n - (phi)^-n where phi is the golden ratio
			default: {
				return Math.round(Math.pow((1+Math.sqrt(5))/2,n) - Math.pow((-1+Math.sqrt(5))/2,n));
			}						
		}
	}
}