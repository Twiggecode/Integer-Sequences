import java.util.Scanner;

public class EulerTotientFunction {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        System.out.println("Phi value for " + n + " is : " + phi(n));
    }

    private static int phi(int n) {
        int res = 1;
        for(int i = 2; i < n; i++){
            if(gcd(i,n) == 1)
                res += 1;
        }
        return res;
    }

    private static int gcd(int a, int b) {
        return (a == 0) ? b : gcd(b%a, a);
    }
}
