import java.util.Scanner;

public class square_numbers {
    private static int nth_square_value(int n) {
        
        return ( n + 1 ) * ( n + 1 );
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the nth value to find :");
        int n = sc.nextInt();
        System.out.println(n + "th value in square numbers sequence is " + nth_square_value((n)));
        sc.close();
    }
}