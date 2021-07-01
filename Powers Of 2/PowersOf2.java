import java.util.Scanner;
import java.util.InputMismatchException;

public class Cater {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int number;
        int n;
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
        
		
		number = (int) Math.pow(2, n);
        System.out.println(number);
		
		
    }

} 
