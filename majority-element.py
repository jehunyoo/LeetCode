class Solution:
    # sort, fast
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
    
    # divide and conquer
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        return [a, b][nums.count(b) > half]

    # collections.Counter
    def majorityElement(self, nums: List[int]) -> int:
        num, count = collections.Counter(nums).most_common(1)[0]
        if count > len(nums) // 2:
            return num
        else:
            return

    # collections.Counter (under condition that the majority element always exists)
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]
    
    # dynamic programming (memoization)
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        for num in nums:
            if count[num] == 0:
                count[num] = nums.count(num)
            if count[num] > len(nums) // 2:
                return num