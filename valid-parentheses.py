class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif stack == []:
                return False
            else:
                if (ch == ')' and stack[-1] == '(') or (ch == ']' and stack[-1] == '[') or (ch == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for ch in s:
            if ch not in table:
                stack.append(ch)
            elif not stack or table[ch] != stack.pop():
                return False
        
        return len(stack) == 0