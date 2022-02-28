class Solution:
    # bit manipulation, binary system
    def hammingDistance(self, x: int, y: int) -> int:
        answer = 0
        z = x ^ y
        while z:
            answer += z % 2
            z //= 2
        return answer
    
    # bit manipulation, string
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')