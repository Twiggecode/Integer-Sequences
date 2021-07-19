import java.util.Scanner;
import java.lang.Math;

public class Cullen_number {

    static long cullen_number(long n){
        return n * (long) Math.pow(2, n) + 1;
    }

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		long result;
		
		while(true){
			System.out.printf("Enter a number: ");
			result = in.nextLong();
			if(result > -1){
				break;
			}
			else{
				System.out.printf("Natural number expected!\n");
			}
		}
		
        System.out.println(cullen_number(result));
		in.close();
	}
	
	
}