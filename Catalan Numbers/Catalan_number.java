import java.util.Scanner;

public class Catalan_number {

    static long catalan_number(long n){
        if (n <= 1){
			return 1;
		}
	
		long result = 0;
	
		for (int i = 0; i < n; i++){
			result += catalan_number(i) * catalan_number(n - i - 1);
		}
	 
		return result;
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
		
        System.out.println(catalan_number(result));
		in.close();
	}
	
	
}