class Solution:
    # collections.Counter: O(nlogn)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item for item, _ in collections.Counter(nums).most_common(k)]
    
    # zip and asterisk
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
    
    # heap: O(nlogn)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = []
        
        for num in counter:
            heapq.heappush(heap, (-counter[num], num))
    
        return [heapq.heappop(heap)[1] for _ in range(k)]