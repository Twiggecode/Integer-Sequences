import java.util.Scanner;

public class SylvesterSequence {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        System.out.println(n + "th value in Sylvester Sequence is :" + seq(n));
    }

    private static int seq(int n) {
        int pdt = 1, ans = 2, N = 1000000007;
        for(int i=1; i<n+1; i++){
            ans = ((pdt % N) * (ans % N)) % N;
            pdt = ans;
            ans = (ans + 1) % N;
        }
        return ans;
    }
}
