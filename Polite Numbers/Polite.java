import java.util.Scanner;

public class Polite {

	// this class returns the nth element of the Polite numbers where n is a positive integer input by the user
	// the polite numbers are the sequence of natural numbers that are not powers of 2
	
	public static void main(String[] args) {
		
		
		int i = 1;
		int count = 0;	
		var scanner = new Scanner(System.in);
		int n;		
		
		// the loop is used to check if the number input by the user is a positive integer
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
		
		
		
		while (count<=n) // count the first n natural numbers that are not powers of 2, which will return the nth polite number
		{
			if((Math.log(i))/(Math.log(2)) != Math.round((Math.log(i))/(Math.log(2)))) // check if a number is not power of 2
			{
				count++;	// count will not increment if the number is a power of 2
			}
			i++;
		}
	
		System.out.print(i-1);
		
	}


}
