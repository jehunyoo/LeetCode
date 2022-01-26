class Solution:
    # two pointers: O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left != right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]

    # binary search without slicing: O(nlogn)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k = 0
        while k < len(numbers): # O(n)
            number = numbers[k]
            index = bisect.bisect_left(numbers, target - number, k + 1) # O(logn)
            if index < len(numbers) and numbers[index] == target - number:
                return [k + 1, index + 1]
            k += 1

    # binary search with slicing: O(nlogn)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k = 0
        while k < len(numbers): # O(n)
            number = numbers[k]
            index = bisect.bisect_left(numbers[k+1:], target - number) # O(logn)
            if k+1+index < len(numbers) and numbers[k+1+index] == target - number:
                return [k + 1, k + 1 + index + 1]
            k += 1