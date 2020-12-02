# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # O(n), O(1)
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None:
            return head

        odd = head
        head_even = even = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = head_even

        return head
