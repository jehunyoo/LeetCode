class Solution:
    # itertools.permutaions
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

    # DFS, tree, recursion
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def search(food=[], ingredients=nums):
            if not ingredients:
                answer.append(food)
                return
            for ingredient in ingredients:
                search(food + [ingredient], [num for num in ingredients if num != ingredient])                
        
        search()
        return answer
    
    # DFS, iteration
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = [([], set())]
        permutations = []
        
        while stack:
            p, used = stack.pop()
            if len(p) == len(nums):
                permutations.append(p)
                continue
            for i, num in enumerate(nums):
                if i not in used:
                    stack.append(([n for n in p] + [num], {idx for idx in used} | {i}))
        
        return permutations