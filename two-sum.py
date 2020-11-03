class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            if target - num in nums_dict:
                return [idx, nums_dict[target - num]]
            nums_dict[num] = idx

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            nums_dict[num] = idx

        for idx, num in enumerate(nums):
            if target - num in nums_dict and idx != nums_dict[target - num]:
                return [idx, nums_dict[target - num]]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            if target - num in nums[idx + 1:]:
                return [idx, idx + nums[idx + 1:].index(target - num) + 1]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums[idx1+1:]):
                if num1 + num2 == target:
                    return [idx1, idx1 + idx2 + 1]

    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for idx1 in range(length):
            for idx2 in range(idx1 + 1, length):
                if nums[idx1] + nums[idx2] == target:
                    return [idx1, idx2]
