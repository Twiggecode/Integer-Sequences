import java.util.Arrays;
import java.util.Scanner;

public class EulerZigZagNumbers {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        System.out.println(n + "th value in Euler's Zig Zag Numbers is :" + zigzag(n));
    }

    private static int zigzag(int n) {
        int[] fact = new int[n + 1];
        int[] zig = new int[n + 1];
        int sum;
        Arrays.fill(fact, 0);
        Arrays.fill(zig, 0);
        fact[0] = 1;
        for (int i = 1; i < n + 1; i++) {
            fact[i] = fact[i - 1] * i;
        }
        zig[0] = 1;
        zig[1] = 1;
        for (int i = 2; i < n; i++) {
            sum = 0;
            for (int k = 0; k < i; k++) {
                sum += (int) ((fact[i - 1] / (fact[i - 1 - k] * fact[k])) * zig[k] * zig[i - 1 - k]);
            }
            zig[i] = (int) sum / 2;
        }
        return zig[n - 1];
    }
}
