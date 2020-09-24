class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch.lower() for ch in s if ch.isalnum()]
        
        return s == s[::-1]
    
    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]

    def isPalindrome3(self, s: str) -> bool:
        s1 = [ch.lower() for ch in s if ch.isalnum()]
        s2 = s1[:]
        s2.reverse()
        
        return s1 == s2

    def isPalindrome4(self, s: str) -> bool:
        p = re.compile('[a-zA-Z0-9]')
        s = list(map(str.lower, p.findall(s)))
        mid = len(s) // 2
        end = len(s) - 1
        
        for idx, ch in enumerate(s[:mid]):
            if ch == s[end - idx]:
                pass
            else:
                return False
        else:
            return True
    
    def isPalindrome5(self, s: str) -> bool:
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