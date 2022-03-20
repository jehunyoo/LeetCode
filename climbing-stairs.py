class Solution:
    # dynamic programming
    def climbStairs(self, n: int) -> int:
        stairs = collections.defaultdict(int)

        for i in range(1, n + 1):
            if i <= 2:
                stairs[i] = i
            else:
                stairs[i] = stairs[i - 1] + stairs[i - 2]

        return stairs[n]
    
    # two variables
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        x, y = 1, 2
        for _ in range(3, n + 1):
            x, y = y, x + y
        
        return y