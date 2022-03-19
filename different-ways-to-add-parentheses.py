class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        for i, op in enumerate(expression):
            if op in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                
                for l in left:
                    for r in right:
                        results.append(eval(f"{l}{op}{r}"))
        
        return results