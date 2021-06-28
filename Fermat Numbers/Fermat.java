import java.util.Scanner;

public class Fermat {

	// this class returns the nth element of the Fermat numbers where n is a positive integer (or zero) input by the user
	
	public static void main(String[] args) {
		
	
		var scanner = new Scanner(System.in);
		int n;			
		// the loop is used to check if the number input by the user is a positive integer or zero
        while (true) {
            System.out.print("Enter a number: ");
            n = scanner.nextInt();	// prompt the user to enter a number
            if (n > -1)
            {
                break;
            }
            System.out.println("Invalid number, please enter a new number.");
        }	
		scanner.close();
			
		System.out.print(Math.round(Math.pow(2,Math.pow(2,n)) +1));		// calculate the Fermat numbers using Fn = 2^(2^n)  + 1			
		
	}

}
