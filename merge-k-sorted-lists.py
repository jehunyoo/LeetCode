# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # heap
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = node = ListNode(None)
        heap = []
        
        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, idx, head))
        
        while heap:
            pop = heapq.heappop(heap)
            idx = pop[1]
            node.next = pop[2]
            node = node.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
            
        return root.next

    # brute force
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or not any(lists):
            return None
        
        answer = node = ListNode(val=None)
        
        while any(lists):
            lists = [head for head in lists if head is not None]
            values = set(head.val for head in lists)
            small = min(values)
            
            for idx, head in enumerate(lists):
                if head and head.val == small:
                    node.next = ListNode(head.val)
                    node = node.next
                    lists[idx] = head.next
        
        return answer.next
                    