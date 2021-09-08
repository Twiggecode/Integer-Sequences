import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        
        int firstNumber = 1;
        int secondNumber = 1;
        int thirdNumber = 1;
                
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter the number of terms for Padovan sequence : ");
        
        int noOfTerms = scanner.nextInt();
        int nextNumber;
        
        System.out.print( firstNumber + " " + secondNumber + " " + thirdNumber);
        
        for(int i = 1; i <= noOfTerms - 3; i++) { 
            
            nextNumber = secondNumber + firstNumber;
            System.out.print(" " + nextNumber);
            firstNumber = secondNumber;
            secondNumber = thirdNumber;
            thirdNumber = nextNumber;
            
        }        


    }

}
