class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch.lower() for ch in s if ch.isalnum()]
        
        return s == s[::-1]

'''
Runtime: 36 ms, faster than 94.93% of Python3 online submissions for Valid Palindrome.
Memory Usage: 19.9 MB, less than 5.03% of Python3 online submissions for Valid Palindrome.
'''