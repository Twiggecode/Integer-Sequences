import java.util.Scanner;

public class CentralBinomialCoefficient {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        int k = n;
        n = 2 * n;
        System.out.println(k + "th value in Central Binomial Coefficient is : " + binomialCoeff(n, k));
    }

    private static int binomialCoeff(int n, int k) {
        int[][] C = new int[n + 1][k + 1];
        int i, j;
        for (i = 0; i <= n; i++) {
            for (j = 0; j <= Math.min(i, k); j++) {
                if (j == 0 || j == i)
                    C[i][j] = 1;
                else
                    C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
            }
        }
        return C[n][k];
    }
}
