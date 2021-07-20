import java.util.Scanner;
import java.lang.Math;

public class Carol_number {

    static long carol(long n){
        n++;
	    return (long) Math.pow((Math.pow(2, n) - 1), 2) - 2;
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
		
        System.out.println(carol(result));
		in.close();
	}
	
	
}