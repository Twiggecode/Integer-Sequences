//This algorithm is to partition it such that all nodes less than x come before nodes greater than or equal to x.

import java.io.*;

class Solution{
	public ListNode partition(ListNode head, int x){
		ListNode small = new ListNode(0);
		ListNode large = new ListNode(0);

		ListNode p1 = small;
		ListNode p2 = large;

		while(head != null){
			if(head.val < x){
				p1.next = head;
				p1 = p1.next;
			}else{
				p2.next = head;
				p2 = p2.next;
			}
			head = head.next;
		}
		p2.next = null;
		p1.next = large.next;
		return small.next;
	}
}

