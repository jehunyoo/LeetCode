# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # O(n), O(1)
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if not head or m == n:
            return head

        index = 1
        node = head
        prev = None
        cut_front = None
        cut_rear = None

        while node:
            if index == m-1:
                cut_front = node
            elif index == m:
                reverse_tail = node
            elif index == n:
                reverse_head = node
            elif index == n+1:
                cut_rear = node

            if m <= index <= n:
                node.next, prev, node = prev, node, node.next
            else:
                prev = node
                node = node.next
            index += 1

        if cut_front:
            cut_front.next = reverse_head
        else:
            head = reverse_head
        reverse_tail.next = cut_rear

        return head

    # start, end, tmp : O(n), O(1)
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head
        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n - m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

        return root.next
