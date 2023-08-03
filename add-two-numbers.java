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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        ListNode node = head;
        int val1, val2, carry = 0;
        while (l1 != null || l2 != null) {
            val1 = l1 != null? l1.val: 0;
            val2 = l2 != null? l2.val: 0;
            node.next = new ListNode((val1 + val2 + carry) % 10);
            node = node.next;
            carry = (int)(val1 + val2 + carry) / 10;
            
            l1 = l1 != null? l1.next: null;
            l2 = l2 != null? l2.next: null;
        }
        if (carry > 0) {
            node.next = new ListNode(carry);
        }

        return head.next;
    }
}