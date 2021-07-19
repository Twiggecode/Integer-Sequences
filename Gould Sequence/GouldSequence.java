import java.util.*;

/**
 * Gould' Sequence Example
 * Row Number                Pascal's triangle                 count of odd numbers in ith row
 * 0th row                             1                                         1
 * 1st row                           1   1                                       2
 * 2nd row                         1   2   1                                     2
 * 3rd row                       1   3   3   1                                   4
 * 4th row                     1   4   6   4   1                                 2
 * 5th row                   1   5   10  10  5   1                               4
 * 6th row                 1   6   15  20  15  6   1                             4
 * 7th row               1   7   21  35  35  21  7   1                           8
 * 8th row             1  8   28   56  70   56  28  8  1                         2
 * 9th row           1   9  36  84  126  126  84  36  9  1                       4
 * 10th row        1  10  45  120 210  256  210 120 45 10  1                     4
 *
 * Code Logic
 *
 * for row=5
 * 5 in binary = 101
 * count of 1's =2
 * 22= 4
 *
 * So, 5th row of pascal triangle will have 4 odd number
 */

public class GouldSequence {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value : ");
        int find_val = scan.nextInt();
        int ans = find_val;
        int count = 0;
        while(find_val != 0){
            count += find_val & 1;
            find_val >>= 1;
        }
        System.out.println(ans + "th row in pascal Triangle has "+ (1 << count) +" odd numbers");
    }
}
