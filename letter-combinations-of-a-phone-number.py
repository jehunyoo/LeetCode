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