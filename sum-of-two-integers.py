class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFF # 16bit integer
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        
        if a > MASK // 2:
            a = ~(a ^ MASK)
        return a
    
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a

        MASK = 0xFFFF # 16bit integer
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        
        shift = len(bin(MASK)[2:]) - 1
        if (a >> shift) & 1:
            a = ~(a ^ MASK)
        return a