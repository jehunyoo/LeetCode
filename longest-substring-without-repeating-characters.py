class Solution:
    # dictionary: O(n), O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        left = 0
        length = 0
        
        for right, ch in enumerate(s):
            if ch in used and left <= used[ch]:
                left = used[ch] + 1
            else:
                length = max(length, right - left + 1)
            used[ch] = right            
        
        return length