import java.util.Scanner;

public class RegularPaperFoldingSequence {
    private static String seq(int n) {
        char[] s = {'1'};
        for (int i = 2; i < n + 1; i++) {
            String temp = "1", prev = "1", zero = "0", one = "1";
            for (int j = 0; j < s.length; j++) {
                temp += s[j];
                if (prev.equals("0")) {
                    temp += one;
                    prev = one;
                } else {
                    temp += zero;
                    prev = zero;
                }
            }
            s = temp.toCharArray();
        }
        return new String(s);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n = scan.nextInt();
        System.out.println(n + "th value in Regular Paper Folding Sequence is " + seq(n));
    }
}
