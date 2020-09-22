class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch.lower() for ch in s if ('A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9')]
        mid = len(s) // 2
        end = len(s) - 1
        
        for idx, ch in enumerate(s[:mid]):
            if ch == s[end - idx]:
                pass
            else:
                return False
        else:
            return True

'''
Runtime: 68 ms, faster than 21.32% of Python3 online submissions for Valid Palindrome.
Memory Usage: 19.9 MB, less than 5.03% of Python3 online submissions for Valid Palindrome.
'''