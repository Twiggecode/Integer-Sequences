import java.util.*;

public class PronicNumbers {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the nth value : ");
        int find_val = scan.nextInt();
        int check = 0;
        int ans = 0;
        int iterator = 1;
        while(check != find_val){
            boolean flag = false;
            for(int i=0; i<iterator+1; i++){
                if(i*(i+1) == iterator){
                    flag = true;
                    break;
                }
            }
            if(flag) {
                check += 1;
                ans = iterator;
            }
            iterator += 1;
        }
        System.out.println(find_val + "th Pronic Number is "+ans);
    }
}
