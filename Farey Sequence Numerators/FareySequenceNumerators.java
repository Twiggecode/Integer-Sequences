import java.util.*;
/**
 * *****************************************
 * Farey Sequence Numerators and Denominators
 * <p>
 * F1 = 0/1, 1/1
 * F2 = 0/1, 1/2, 1/1
 * F3 = 0/1, 1/3, 1/2, 2/3, 1/1
 * .
 * .
 * .
 * F7 = 0/1, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 2/5,
 * 3/7, 1/2, 4/7, 3/5, 2/3, 5/7, 3/4, 4/5,
 * 5/6, 6/7, 1/1
 * <p>
 * *****************************************
 */


class FareySequenceNumerators {

    static void fareySequence(int n) {
        // We know first two terms are 0/1 and 1/n
        double x1 = 0, y1 = 1, x2 = 1, y2 = n;

        System.out.printf("%.0f %.0f", x1, x2);

        double x, y = 0; // For next terms to be evaluated
        while (y != 1.0) {
            // Using recurrence relation to find the next term
            x = Math.floor((y1 + n) / y2) * x2 - x1;
            y = Math.floor((y1 + n) / y2) * y2 - y1;

            // Print next term
            System.out.printf(" %.0f", x, y);

            // Update x1, y1, x2 and y2 for next iteration
            x1 = x2;
            x2 = x;
            y1 = y2;
            y2 = y;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the term number to generate : ");
        int n = sc.nextInt();
        fareySequence(n);
    }
}