class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    def arrayPairSum2(self, nums: List[int]) -> int:
        answer = 0
        for idx, num in enumerate(sorted(nums)):
            if idx % 2 == 0:
                answer += num
        return answer

    def arrayPairSum3(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for idx in range(0, len(nums), 2):
            answer += nums[idx]
        return answer
