class Solution:
    # dynamic programming, memoization
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0

        return max(nums)

    # Kadane's algorithm: O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        
        return best_sum

    # Time Limit Exceeded
    def maxSubArray(self, nums: List[int]) -> int:
        def findSubArray(lrange, rrange, sums):
            if lrange == rrange:
                return sums

            left = findSubArray(lrange, rrange - 1, sums - nums[rrange])
            right = findSubArray(lrange + 1, rrange, sums - nums[lrange])

            return max(left, right, sums)
        
        return findSubArray(0, len(nums) - 1, sum(nums))