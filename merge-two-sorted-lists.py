# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # iteration : O(n), O(n)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif l1 and not l2:
            head = l1
            l1 = l1.next
        elif l2 and not l1:
            head = l2
            l2 = l2.nexat
        elif l1.val <= l2.val:
            head = l1
            l1 = l1.next
        elif l1.val > l2.val:
            head = l2
            l2 = l2.next

        node = head
        while l1 or l2:

            if l1 and not l2:
                node.next = l1
                l1 = l1.next
            elif l2 and not l1:
                node.next = l2
                l2 = l2.next
            elif l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                node.next = l2
                l2 = l2.next

            node = node.next

        return head

    # recursion : O(n), O(1)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
