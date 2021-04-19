class Solution:
    # sort
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

    # heapq.nlargest
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    # heapq.heapify
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k + 1):
            kth = heapq.heappop(nums)
        
        return kth

    # heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        for _ in range(k):
            kth = -heapq.heappop(heap)
        
        return kth