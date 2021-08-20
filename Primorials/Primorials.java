import java.util.*;

public class Primorials {
    public static int MAX = 1000000;

    // vector to store all prime less than and equal to 10^6
    static ArrayList<Integer> primes = new ArrayList<Integer>();

    static void sieveSundaram() {
        boolean[] marked = new boolean[MAX];

        for (int i = 1; i <= (Math.sqrt(MAX) - 1) / 2; i++) {
            for (int j = (i * (i + 1)) << 1; j <= MAX / 2; j += 2 * i + 1) {
                marked[j] = true;
            }
        }
        primes.add(2);

        for (int i = 1; i <= MAX / 2; i++) {
            if (marked[i] == false) {
                primes.add(2 * i + 1);
            }
        }
    }

    // Function to calculate primorial of n
    static int calculatePrimorial(int n) {
        int result = 1;
        for (int i = 0; i < n; i++) {
            result = result * primes.get(i);
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        sieveSundaram();
        System.out.println("Primorial(P#) of " + n + " is " + calculatePrimorial(n));
    }
}
