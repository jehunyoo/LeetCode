# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # move all nodes to l1, swap : O(n), O(1)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        tail = l2
        q = 0

        while l1:
            val = l1.val + l2.val + q if l2 else l1.val + q
            q, r = val // 10, val % 10

            l1.val = r
            last = l1

            if l2 is None:
                l1 = l1.next
            elif l1.next is None and l2:  # swap
                l1.next, l2.next = l2.next, l1.next
                l1, l2 = l1.next, l2.next
            else:
                l1, l2 = l1.next, l2.next
        if q:
            last.next = tail
            tail.val = q
            tail.next = None

        return head

    # use ListNode() : O(n), O(n)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            ssum = 0
            if l1:
                ssum += l1.val
                l1 = l1.next
            if l2:
                ssum += l2.val
                l2 = l2.next

            carry, val = divmod(ssum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next
