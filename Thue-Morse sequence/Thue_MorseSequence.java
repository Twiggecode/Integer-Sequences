import java.util.Scanner;

public class Thue_MorseSequence {

    private static String complement(String str){
        String comp = "";
        for(int i=0; i<str.length(); i++){
            comp += (str.charAt(i) == '0') ? '1' : '0';
        }
        return comp;
    }

    private static String seq(int n){
        String s = "0";
        for(int i=1; i<n; i++){
            s += complement(s);
        }
        return s;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value to find : ");
        int n  = scan.nextInt();
        System.out.println(n + "th value in Thue-Morse Sequence is : "+ seq(n));
    }
}
