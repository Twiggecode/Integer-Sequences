import java.util.Scanner;

public class Motzkin_Numbers {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        System.out.println(n + "th value in Motzkin Numbers is  : " + Motzkin(n));
    }

    private static int Motzkin(int n) {
        if (n == 0 || n == 1) return 1;
        return ((2 * n + 1) * Motzkin(n - 1) + (3 * n - 3) * Motzkin(n - 2)) / (n + 2);
    }
}
