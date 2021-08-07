/* Narayana's Cows Sequence
Formula: f(x) = f(x-1) + f(x-3)
First few terms of the sequence: 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, ... */

import java.util.*;

public class Narayan_cows 
{  
    public static void main(String[] args)  { 
        System.out.print("Enter a whole number to return the element at that index in the Narayana's Cows sequence: "); 
        Scanner sc = new Scanner(System.in); 
        int input = sc.nextInt();

        while (input <  0) {                                  //Checking that the input is a whole number
        System.out.print("Please enter a whole number only: "); 
        input = sc.nextInt();
        }
        
        System.out.println("The number at that index is: "+ narayanas_cows(input));
        }

    public static int narayanas_cows(int input) {
            if (input < 3)
                return 1;
            else 
                return narayanas_cows(input-3) + narayanas_cows(input-1);
        }
}  