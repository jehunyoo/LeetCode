class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]

'''
Runtime: 44 ms, faster than 80.09% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.4 MB, less than 19.12% of Python3 online submissions for Valid Palindrome.
'''