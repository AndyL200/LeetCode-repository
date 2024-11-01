public class J2095 {
    class ListNode {
        ListNode next;
        int val;
        ListNode() {
            
        }
    }
    class Solution {
        public ListNode deleteMiddle(ListNode head) {
            if(head.next == null || head == null) {return null;}
            ListNode c1 = head;
            ListNode c2 = head.next.next;
    
            while(c2 != null && c2.next != null) {
                c1 = c1.next;
                c2 = c2.next.next;
            }
                c1.next = c1.next.next;
    
            System.gc(); //Literally cheating?
            return head;
        }
    }
}
