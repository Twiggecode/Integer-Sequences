import java.util.Scanner;

public class SumOfProperDivisors {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        System.out.println(n + "th value in sum of all divisors is :" + seq(n));
    }

    private static int seq(int n) {
        int res = 0;
        int i = 2;
        while(i <= Math.sqrt(n)){
            if(n % i == 0){
                res = (i == (n/i)) ? res+i : res + (i + (n/i));
            }
            i += 1;
        }
        return (res+1);
    }
}
