import java.util.InputMismatchException;
import java.util.Scanner;

// this class will return the nth prime number, where n is a positive integer (or zero) input by the user

public class Primes {

	public static void main(String[] args) {
		
		var scanner = new Scanner(System.in);
		int n=-1;
		int counter=-1;
		int i=2;
				
		while (true) {
            System.out.print("Enter a number: ");

            try
            {
            	n = scanner.nextInt();	// prompt the user to enter a number
            	
            	if (n > -1) 
                {
                    break;  // if an integer greater than -1 is inputed, we break the loop
                }
                System.out.println("Invalid input, please enter a positive number or 0."); // if an integer less than zero is inputed, the loop will not be broken and this line will be printed
                
            }    
            
            catch(InputMismatchException e) // enter this catch block if a non integer is input
            {
            	System.out.println("Invalid input, input must be an integer");
            	scanner.next(); // call scanner.next() to prevent an infinite loop
            }          
        }	
		scanner.close();

		while(counter<n)	// iterate through the set of natural numbers counting how many prime numbers are encountered
		{
			
			if (isPrime(i))
					{
						counter++;
					}			
			i++;
		}
				
		System.out.println(i-1);
		
	}

	
	
	public static boolean isPrime (double x)	// a method to detect whether a number is prime or not
	{
		
		for (int i=2; i<(x/2)+1; i++) // loop over all natural numbers that precede the number that you are checking to be prime or not
		{
			if (x % i == 0)	// if the number is found to be divisible by a natural number that proceeds it, the number is not prime
			{
				return false;
			}
		}
		
		return true;	// else, the number is prime
	}
	
	
}
