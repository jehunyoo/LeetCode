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
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head;
        ListNode rev = null, temp;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            if (rev == null)
                temp = rev;
            else
                temp = new ListNode(rev.val, rev.next);

            rev = new ListNode(slow.val);
            rev.next = temp;
            slow = slow.next;
        }
        if (fast != null) {
            slow = slow.next;
        }

        while (rev != null && rev.val == slow.val) {
            rev = rev.next;
            slow = slow.next;
        }

        if (rev == null)
            return true;
        else
            return false;
    }

    public boolean isPalindrome(ListNode head) {
        ListNode node = head;
        ArrayList<Integer> list = new ArrayList<>();
        int top = -1, bot = 0;

        while (node != null) {
            list.add(node.val);
            top++;
            node = node.next;
        }

        while (bot < top && list.get(bot) == list.get(top)) {
            bot++;
            top--;
        }

        if (bot >= top)
            return true;
        else
            return false;
    }
}