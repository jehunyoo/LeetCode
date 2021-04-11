# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        answer = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node is None:
                continue
            elif low <= node.val <= high:
                answer += node.val
                stack.append(node.left)
                stack.append(node.right)
            elif node.val > high:
                stack.append(node.left)
            elif node.val < low:
                stack.append(node.right)
        
        return answer