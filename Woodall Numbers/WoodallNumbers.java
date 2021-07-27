import java.util.Scanner;
import java.lang.Math;

/**
 * #Formula: n*2n − 1, with n ≥ 1.
 * #Example : {1, 7, 23, 63, 159, 383, 895, 2047, 4607, ...}
 * #Input of 0 for n = 1, 1 for n = 2...
 */

public class WoodallNumbers {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        System.out.println(n + "th value of Woodall number is " + (int)((n+1) * Math.pow(2,(n+1)) - 1));
    }
}
