using System;

class Program  
{  
    static void Main(string[] args)  
    {  
    	 Console.WriteLine("The Nth term in the sequence is " + powerOf2()); 	        

        Console.ReadLine();
    }  

    public static int userInput() {
		while(true) {
			try {
				Console.WriteLine("Enter the value of n: ");
				int n = int.Parse(Console.ReadLine());
				return n;
			}
			catch(Exception e) {
				Console.WriteLine("Invalid input: Please enter an integer input.\n" + e);
			}
		}
	}

    public static int powerOf2() {
		int number;
		int n;
		
		while (true){
            
            try
            {
            	n = userInput();	// prompt the user to enter a number
            	
            	if (n > -1) 
                {
                    break;  // if an integer greater than -1 is inputed, we break the loop
                }
                Console.WriteLine("Invalid input, please enter a positive number or 0."); // if an integer less than zero is inputed, the loop will not be broken and this line will be printed
                
            }    
        
            catch(Exception e) // enter this catch block if a non integer is input
            {
            	Console.WriteLine("Invalid input, input must be an integer" + e);
            }          
        }	

		number = (int) Math.Pow(2, n);
        return number;
	} 
}
