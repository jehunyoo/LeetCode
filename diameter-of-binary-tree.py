# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS, recursion: O(n)
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0
        def dfs(node=root):
            if node.left is None and node.right is None:
                return 1
            left = dfs(node.left) if node.left is not None else 0
            right = dfs(node.right) if node.right is not None else 0
            nonlocal diameter
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        
        dfs()
        return diameter