class Solution:
    # Bit Manipulation: O(1), O(1)
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer
            