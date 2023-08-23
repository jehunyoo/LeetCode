/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null)
            return head;

        ListNode slow = head, fast = head;
        while(fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode half = slow.next;
        slow.next = null;

        ListNode left = sortList(head);
        ListNode right = sortList(half);
        
        ListNode root = new ListNode();
        ListNode node = root;

        while(left != null && right != null) {
            if(left.val < right.val) {
                node.next = left;
                left = left.next;
            } else {
                node.next = right;
                right = right.next;
            }
            node = node.next;
        }
        while(left != null) {
            node.next = left;
            node = node.next;
            left = left.next;
        }
        while(right != null) {
            node.next = right;
            node = node.next;
            right = right.next;
        }
       
        return root.next;
    }
}