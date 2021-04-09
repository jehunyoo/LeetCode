# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        path = 0
        
        def dfs(node=root):
            if node.left is None and node.right is None:
                return 0
            
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
            
            left = left + 1 if node.left and node.val == node.left.val else 0
            right = right + 1 if node.right and node.val == node.right.val else 0
                
            nonlocal path
            path = max(path, left + right)
            return max(left, right)
        
        dfs()
        return path