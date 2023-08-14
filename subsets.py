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

    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack = [([], None)]
        answer = []
        while stack:
            sub, large = stack.pop()
            answer.append(sub)
            for num in nums:
                if large is None or (large is not None and large < num):
                    stack.append(([n for n in sub] + [num], num))
        
        return answer