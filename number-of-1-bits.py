class Solution:
    # bit manipulation, & operation (n & n - 1)
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

    # bit manipulation, string
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    # bit manipulation, string
    def hammingWeight(self, n: int) -> int:
        return bin(n & 0xFFFFFFFF).count('1')