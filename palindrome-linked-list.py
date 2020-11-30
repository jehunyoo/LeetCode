# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # linked list, runner : O(n), O(1)
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        rev = None

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast is not None:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev

    # list : O(n), O(n)
    def isPalindrome2(self, head: ListNode) -> bool:
        numbers = []
        node = head
        while node is not None:
            numbers.append(node.val)
            node = node.next
        return numbers == numbers[::-1]
