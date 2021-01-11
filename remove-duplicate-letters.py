class Solution:
    # stack, set, Counter: O(n), O(n)
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        counter = collections.Counter(s)
        
        for ch in s:
            counter[ch] -= 1
            if ch in seen:
                continue
            
            while stack and stack[-1] > ch and counter[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
        
        return ''.join(stack)

    # strange stack: O(n^2), O(n)
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        
        for i, ch in enumerate(s):
            if not stack:
                stack.append(ch)
            elif ch not in stack:
                while stack and stack[-1] > ch and stack[-1] in s[i+1:]:
                    stack.pop()
                stack.append(ch)
        
        return ''.join(stack)

    # recursion: O(n^2), O(n)
    def removeDuplicateLetters(self, s: str) -> str:
        for ch in sorted(set(s)):
            suffix = s[s.index(ch):]
            if set(s) == set(suffix):
                return ch + self.removeDuplicateLetters(suffix.replace(ch, ''))
        return ''