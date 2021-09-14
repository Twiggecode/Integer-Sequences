import java.util.*;
public class Main 
{
    static int divsum(int n) 
    {
        int sum = 0;
        for (int i = 1; i <= (Math.sqrt(n)); i++) {
            if (n % i == 0) {
 
                if (n / i == i) {
                    sum = sum + i;
                } else {
                    sum = sum + i;
                    sum = sum + (n / i);
                }
            }
        }
        return sum;
    }
 
    static boolean isDeficientNumber(int n) 
    {
        return (divsum(n) < (2 * n));
    }
 
    public static void main(String args[]) {
        int n ;
        Scanner sc = new Scanner (System.in);
        n = sc.nextInt();
        for (int i =0 ; i < n ; i ++){
            if (isDeficientNumber(i))
                System.out.print(i+", ");
        }
    }
}
