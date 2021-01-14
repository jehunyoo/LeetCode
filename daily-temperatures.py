class Solution:
    # stack: O(n), O(n)
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        warm = [0 for _ in range(len(T))]
        
        for idx, temp in enumerate(T):
            if not stack or stack[-1][1] >= temp:
                stack.append((idx, temp))                
            elif stack[-1][1] < temp:
                while stack and stack[-1][1] < temp:
                    top = stack.pop()
                    warm[top[0]] = idx - top[0]
                stack.append((idx, temp))
        
        return warm