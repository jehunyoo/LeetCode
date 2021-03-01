class Solution:
    # combination with repetition, efficient
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def search(elements=[], index=0):
            if sum(elements) == target:
                answer.append(elements)
                return
            for i in range(index, len(candidates)):
                candidate = candidates[i]
                if sum(elements) + candidate <= target:
                    search(elements + [candidate], i)
        
        search()
        return answer

    # combinaiton with repetition
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        def search(elements=[]):
            if sum(elements) == target:
                answer.append(elements)
                return
            for candidate in candidates:
                if elements and max(elements) <= candidate and sum(elements) + candidate <= target:
                    search(elements + [candidate])
                elif not elements and sum(elements) + candidate <= target:
                    search(elements + [candidate])
        
        search()
        return answer

    # permutation, slow
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def search(elements=[]):
            if sum(elements) == target and sorted(elements) not in answer:
                answer.append(sorted(elements))
                return
            for candidate in candidates:
                if sum(elements) + candidate <= target:
                    search(elements + [candidate])
        
        search()
        return answer