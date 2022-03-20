class Solution:
    def rob(self, nums: List[int]) -> int:
        money = collections.defaultdict(int)
        
        for i, num in enumerate(nums):
            money[i] = num + max(money[i -  2], money[i - 3])
        
        return max(money[len(nums) - 1], money[len(nums) - 2])