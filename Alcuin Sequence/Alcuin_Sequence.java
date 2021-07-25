import java.util.Scanner;

/**
 * Alcuin Sequence
 * Formula: a(n) = round(n^2/12) – floor(n/4)*floor((n+2)/4)
 * Example: 0, 0, 0, 1, 0, 1, 1, 2, 1, 3, 2, 4, 3, 5, 4, 7 ...
 */

public class Alcuin_Sequence {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        System.out.println(n + "th value in Alcuin's Sequence is " + Alcuin(n));
    }

    private static int Alcuin(int _n) {
        double n = _n;
        return (int)(Math.round((n * n) / 12) - Math.floor(n / 4) * Math.floor((n + 2) / 4));
    }
}
