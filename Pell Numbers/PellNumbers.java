import java.util.Scanner;

/**
 * Pell's Numbers
 * Formula : Pn = 2*Pn-1 + Pn-2 where P0 = 0 and P1 = 1
 * Example : 0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, ....
 */
public class PellNumbers {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        System.out.println(n + "th value in Pell's Number is " + pell(n));
    }

    private static int pell(int n) {
        if(n <= 2){
            return n;
        }
        int first = 1, second = 2,  i = 3, tmp;
        while(i <= n){
            tmp = 2 * second + first;
            first = second;
            second = tmp;
            i += 1;
        }
        return second;
    }
}
