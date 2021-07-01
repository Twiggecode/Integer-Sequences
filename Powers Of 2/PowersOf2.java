import java.util.Scanner;

public class PowersOf2 {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int number;
        int n;
        do{
            System.out.println("Insert a number that is greater than or equal to zero:");
            n = scanner.nextInt();
            if(n < 0){
                System.out.println("Invalid entry, please try again");
            }
        } while(n < 0);

        number = (int) Math.pow(2, n);
        System.out.println(number);
        scanner.close();
    }

}