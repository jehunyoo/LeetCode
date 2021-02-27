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