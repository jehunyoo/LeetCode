class Solution:
    # bisect.bisect_left
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
 
    # iteration
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        
        while low != high:
            index = low + (high - low) // 2
            # index = (low + high) // 2 # overflow
            if nums[index] < target:
                low = index + 1
            elif nums[index] > target:
                high = index
            elif nums[index] == target:
                return index
        
        return -1

    # recursion
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low=0, high=len(nums)):
            if low == high:
                return -1
            
            index = low + (high - low) // 2
            # index = (low + high) // 2 # overflow
            if nums[index] < target:
                index = binary_search(index + 1, high)
            elif nums[index] > target:
                index = binary_search(low, index)
            
            return index
        
        return binary_search()