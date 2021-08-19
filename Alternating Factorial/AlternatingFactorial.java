package Alternating_Factorial;

public class AlternatingFactorial {
        
    public static double alternatingFactorial(int n) {
        double value = 0.0;

        try {
            if (n < 1) {
                throw new Exception("Input value must be greater than or equal to 1");
            }
            
            value = altFatorialHelper(n, n);    

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        return value;
    }


    private static double altFatorialHelper(int n, int i) {
        // n: will never change.
        // i: will iterate [n, (n-1), ..., 1]
        if (i == 1) {
            return Math.pow(-1, n-1);
        }

        return Math.pow(-1, n-i) * factorial(i) + altFatorialHelper(n, i-1);
    }


    private static double factorial(int n) {
        if (n == 1) {
            return 1;
        }

        return n * factorial(n-1);
    }

    public static void main(String[] args) {
        System.out.println(alternatingFactorial(0));
        System.out.println(alternatingFactorial(1));
        System.out.println(alternatingFactorial(2));
        System.out.println(alternatingFactorial(3));
        System.out.println(alternatingFactorial(4));
        System.out.println(alternatingFactorial(5));
        System.out.println(alternatingFactorial(6));
        System.out.println(alternatingFactorial(7));
        System.out.println(alternatingFactorial(8));
        System.out.println(alternatingFactorial(9));
        System.out.println(alternatingFactorial(10));
    }
}