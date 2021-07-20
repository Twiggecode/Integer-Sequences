import java.util.*;

/**
 * Perrin Sequence
 * P(n) = P(n−2) + P(n−3) for n ≥ 3, with P(0) = 3, P(1) = 0, P(2) = 2.
 * Example : {3, 0, 2, 3, 2, 5, 5, 7, 10, 12, ...}
 */
public class PerrinNumbers {
    public static int perrinSequence(int n){
        int tmp = 0;
        int first = 3, second = 0, third = 2;
        if(n == 0){
            return first;
        }
        if(n == 1){
            return second;
        }
        if(n == 2){
            return third;
        }
        while(n > 2){
            tmp = first + second;
            first = second;
            second = third;
            third = tmp;
            n -= 1;
        }
        return tmp;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value : ");
        int find_val = scan.nextInt();
        System.out.println(find_val + "th value in Perrin Sequence is " + perrinSequence(find_val));
    }
}
