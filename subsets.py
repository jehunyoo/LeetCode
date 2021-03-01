class Solution:
    # combinations, DFS
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def search(subset=[], index=0):
            answer.append(subset)
            for i in range(index, len(nums)):
                num = nums[i]
                search(subset + [num], i + 1)
        
        search()
        return answer
    
    # itertools.combinations
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [subset for k in range(len(nums) + 1) for subset in itertools.combinations(nums, k)]