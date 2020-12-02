# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # iteration: O(n), O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        prev = None

        while node and node.next:
            post = node.next.next
            # swap
            node, node.next = node.next, node

            # link front
            if prev:
                prev.next = node
            else:
                head = node
            prev = node.next

            # link rear
            node.next.next = post

            # move to next pair
            node = post

        return head

    # recursion : O(n), O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            post = head.next.next
            head, head.next = head.next, head
            head.next.next = self.swapPairs(post)
        return head

    # recursion : O(n), O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head

    # swap values : O(n), O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head
