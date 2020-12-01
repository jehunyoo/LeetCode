# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # iteration : O(n), O(n)
    def reverseList(self, head: ListNode) -> ListNode:
        tail = None
        while head:
            tail, tail.next, head = head, tail, head.next
        return tail

    # recursion : O(n), O(n)
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(head: ListNode, tail: ListNode = None):
            if not head:
                return tail
            post, head.next = head.next, tail
            return reverse(post, head)
        return reverse(head)
