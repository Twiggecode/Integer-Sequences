import java.util.Scanner;

public class Lucas {

	// this class returns the nth element of the Lucas numbers where n is a positive integer (or zero) input by the user
	
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
		

		if (n==0)	// L0 is equal to 2
		{
			System.out.print(2);
		}
		
		else if (n==1)	// L1 is equal to 1
		{
			System.out.print(1);
		}
		
		else if (n==2)	// L2 is equal to 3
		{
			System.out.print(3);
		}
		
		else	// else n is greater than 2, and we use Ln = phi^n - (phi)^-n	    where phi is the golden ratio
		{
			System.out.print(Math.round(Math.pow((1+Math.sqrt(5))/2,n) - Math.pow((-1+Math.sqrt(5))/2,n)));
			
		}						
	}
}
