import java.util.*;

public class JacobsthalNumbers {
    public static int Jacobsthal_Num(int n){
        var dp = new int[n+2];
        dp[0] = 0;
        dp[1] = 1;
        for(int i=2; i<n+1; i++){
            dp[i] = dp[i-1] + 2*dp[i-2];
        }
        return dp[n];
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find :");
        int n = scan.nextInt();
        System.out.println(n + "th value in Jacobsthal Number is " + Jacobsthal_Num(n));
    }
}
