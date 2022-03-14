class Solution:
    # two pointers
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        lptr = lwin = rwin = 0
        
        for rptr, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            
            if not missing:
                while lptr < rptr and need[s[lptr]] < 0:
                    need[s[lptr]] += 1
                    lptr += 1
                
                if rwin == 0 or rptr - lptr <= rwin - lwin:
                    lwin, rwin = lptr, rptr
                    need[s[lptr]] += 1
                    missing += 1
                    lptr += 1
        
        return s[lwin:rwin]

    # counter & operation
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        counter = collections.Counter()
        
        lwin, rwin = float('-inf'), float('inf')
        lptr = 0
        
        for rptr, char in enumerate(s, 1):
            counter[char] += 1
            while counter & need == need:
                if rptr - lptr < rwin - lwin:
                    rwin, lwin = rptr, lptr
                counter[s[lptr]] -= 1
                lptr += 1
        
        return s[lwin:rwin] if rwin - lwin <= len(s) else ''