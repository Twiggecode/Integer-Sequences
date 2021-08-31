import java.util.Scanner;

public class LazyCatererSequence {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        int ans = ((n * (n + 1)) / 2 + 1);
        System.out.println("A circular pizza can be divided into " + ans + " pieces with " + Integer.toString(n) + " cuts!");
    }
}
