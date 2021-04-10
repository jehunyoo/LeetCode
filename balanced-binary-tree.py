# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS, recursion
    def isBalanced(self, root: TreeNode) -> bool:
        height_balance = True
        
        def dfs(node=root):
            if node is None:
                return 0
            if not node.left and not node.right:
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            nonlocal height_balance
            if abs(left - right) > 1:
                height_balance = False
            
            return max(left, right) + 1
        
        dfs()
        return height_balance