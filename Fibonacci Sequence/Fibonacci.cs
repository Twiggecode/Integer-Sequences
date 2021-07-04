using System;

class Program  
{  
    static void Main(string[] args)  
    {  
    	 Console.WriteLine("The Nth term in the sequence is " + fibonacci()); 	        

        Console.ReadLine();
    }  

    public static int userInput() {
		while(true) {
			try {
				Console.WriteLine("Enter the value of n: ");
				int n = int.Parse(Console.ReadLine());
				n += 1;
				return n;
			}
			catch(Exception e) {
				Console.WriteLine("Invalid input: Please enter an integer input.\n" + e);
			}
		}
	}

    public static int fibonacci() {
		// Initialize the first three sequence values
		int n = userInput();
		n += 1;
		int i = 1;

		int num1 = 0, num2 = 1, sum = 0;

		switch(n) {
			// Return the 0th element of the sequence for input=0
			case 1: {
				return 0;
			}
			// Return the 0th element of the sequence for input=1
			case 2: {
				return 1;
			}
			
			default: {
				// Intiliaze the fourth value so it can be returned outside the for loop
				while (i < n - 1){
					sum = num1 + num2;
					num1 = num2;
					num2 = sum;
					i ++;
				}
				return sum;
			}
		}
} 
}
