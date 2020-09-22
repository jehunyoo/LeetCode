class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = [ch.lower() for ch in s if ch.isalnum()]
        s2 = s1[:]
        s2.reverse()
        
        return s1 == s2

'''
Runtime: 52 ms, faster than 54.94% of Python3 online submissions for Valid Palindrome.
Memory Usage: 19.7 MB, less than 7.71% of Python3 online submissions for Valid Palindrome.
'''