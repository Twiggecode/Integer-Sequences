package kolakoski_sequence;

import java.util.LinkedList;
import java.util.List;

public class KolakoskiSequence {
    
    public static List<Integer> kolakoskiSequence(int n) {

        // n: represents the number of "runs" or "blocks"
        
        LinkedList<Integer> list = new LinkedList<Integer>();

        try {

            if (n < 1) {
                throw new Exception("Input value must be greater than or equal to 1");
            }

            if (n >= 1) { list.addLast(1); }
            if (n >= 2) { list.addLast(2); }
            if (n >= 3) { list.addLast(2); }

            if (n > 3) {
                LinkedList<Integer> block = new LinkedList<Integer>();
                block.add(2);

                list = kSequenceHelper(n, 4, list, block);
            }

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        return list;
    }

    private static LinkedList<Integer> kSequenceHelper(int n, int iter, LinkedList<Integer> list, LinkedList<Integer> block) {
        if (iter > n) {
            return list;
        }

        int nextDigit = list.peekLast() % 2 + 1;
        LinkedList<Integer> newBlock = new LinkedList<Integer>();
        
        for (int i : block) {

            for (int j = 1; j <= i; j++) {
                list.addLast(nextDigit);
                newBlock.addLast(nextDigit);
            }
            
            nextDigit = nextDigit % 2 + 1;
        }

        return kSequenceHelper(n, iter+1, list, newBlock);
    }

    public static void main(String[] args) {
        List<Integer> list;
        
        list = kolakoskiSequence(0);
        System.out.println(list.toString());

        list = kolakoskiSequence(1);
        System.out.println(list.toString());

        list = kolakoskiSequence(2);
        System.out.println(list.toString());
        
        list = kolakoskiSequence(3);
        System.out.println(list.toString());

        list = kolakoskiSequence(4);
        System.out.println(list.toString());

        list = kolakoskiSequence(5);
        System.out.println(list.toString());

        list = kolakoskiSequence(6);
        System.out.println(list.toString());
    }
}