class Solution:
    # O(n), O(1)
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for _ in range(n):
            x, y = y, x + y
        
        return x

    # iteration, dynamic programming, tabulation, space complexity = O(n)
    def fib(self, n: int) -> int:
        F = [0, 1]
        
        for i in range(2, n + 1):
            F.append(F[i - 1] + F[i - 2])
        
        return F[n]
    
    # recursion, dynamic programming, memoization, space complexity = O(n)
    F = collections.defaultdict(int)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        if self.F[n]:
            return self.F[n]
        
        self.F[n] = self.fib(n - 1) + self.fib(n - 2)
        
        return self.F[n]
    
    # recursion
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)