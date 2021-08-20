import java.util.Scanner;

/**
 * # Idea : Every current term is dependent on previous term
 * # Example : 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
 * # 1 is read off as "one 1" or 11.
 * # 11 is read off as "two 1s" or 21.
 * # 21 is read off as "one 2, then one 1" or 1211.
 * # 111221 is read off as "three 1s, two 2s, then one 1" or 312211.
 */

public class LookAndSaySequence {
    private static String seq(int n){
        if(n == 1)    return "1";
        if(n == 2)    return "11";
        String s = "11";
        for(int i=3; i <= n; i++){
            s += "$";
            int len = s.length();
            int count = 1;
            String tmp = "";
            char[] arr = s.toCharArray();
            for(int j=1; j < len; j++){
                if(arr[j] != arr[j-1]){
                    tmp += count + 0;
                    tmp += arr[j-1];
                    count = 1;
                }
                else{
                    count += 1;
                }
            }
            s = tmp;
        }
        return s;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n  = scan.nextInt();
        System.out.println(n + "th value in Look and Say Sequence is : "+ seq(n));
    }
}
