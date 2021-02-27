class Solution:
    # itertools.combinations
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))
    
    # DFS
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def search(elements=[], start=1):
            if len(elements) == k:
                answer.append(elements)
            for element in range(start, n + 1):
                search(elements + [element], element + 1)
        
        search()
        return answer

    # DFS, tree, recursion
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def search(food=[], ingredients=range(1, n+1)):
            if len(food) == k:
                answer.append(food)
            for ingredient in ingredients:
                search(food + [ingredient], [num for num in ingredients if num > ingredient])
        
        search()
        return answer

    # using permutations, very inefficient: Time Limit Exceeded
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        
        def search(food=[], ingredients=range(1, n+1)):
            if len(food) == k:
                answer.append(food)
                return
            for ingredient in ingredients:
                search(food + [ingredient], [num for num in ingredients if num != ingredient])
        
        search()
        return list(map(list, set(map(frozenset, answer))))