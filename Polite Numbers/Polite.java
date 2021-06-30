import java.util.InputMismatchException;
import java.util.Scanner;

public class Polite {

	// This class returns the nth element of the Polite numbers where n is a positive integer input by the user
	// The polite numbers are the sequence of natural numbers that are not powers of 2
	
	public static void main(String[] args) {
		System.out.println("The Nth element of the Polite numbers is " + polite());
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

	public static long polite() {
		int i = 1;
		int count = 0;
		int n = userInput();
		// Count the first n natural numbers that are not powers of 2, which will return the nth polite number
		while (count<=n) {
			// Check if a number is not power of 2
			if((Math.log(i))/(Math.log(2)) != Math.round((Math.log(i))/(Math.log(2)))) {
				// Count will not increment if the number is a power of 2
				count++;	
			}
			i++;
		}
		return(i-1);
	}
}
