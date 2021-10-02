import java.util.Scanner;
public class Golomb
{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the nth number you want in the Golomb Sequence");
        int n=sc.nextInt();
        int x=golomb(n);
        System.out.println("The "+n+"th Golomb number is: "+x);
        sc.close();
    }
    public static int golomb(int n)
    {
        if(n==1)
            return 1;
        return 1+golomb(n-golomb(golomb(n-1)));
    }
}