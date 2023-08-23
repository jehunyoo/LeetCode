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
    public ListNode insertionSortList(ListNode head) {
        ListNode node = head.next;
        head.next = null;
        while(node != null) {
            ListNode sorted = head, prev = null;
            while(sorted != null && sorted.val < node.val) {
                prev = sorted;
                sorted = sorted.next;
            }
            ListNode temp = node.next;
            if(prev != null) {
                prev.next = node;
                node.next = sorted;
            } else {
                node.next = head;
                head = node;
            }
            node = temp;
        }

        return head;
    }
}