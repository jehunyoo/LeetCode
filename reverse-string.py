class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
    
    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
    
    def reverseString3(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s) // 2
        end = len(s) - 1
        for idx, ch in enumerate(s[:mid]):
            s[idx] = s[end - idx]
            s[end - idx] = ch