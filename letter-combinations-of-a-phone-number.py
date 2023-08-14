class Solution:
    # tree, recursion: O(3^n)
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                 '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        answer = []
        
        if not digits:
            return answer
        
        def search(string="", depth=0):
            if depth == len(digits):
                answer.append(string)
                return
            for letter in phone[digits[depth]]:
                search(string + letter, depth + 1)
        
        search()
        return answer

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapper = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        stack = [""]
        answer = []
        while stack:
            s = stack.pop()
            if len(s) == len(digits):
                answer.append(s)
                continue
            for ch in mapper[digits[len(s)]]:
                stack.append(s + ch)
        
        return answer