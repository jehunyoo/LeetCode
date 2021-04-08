# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS, iteration: O(n)
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if root is None:
            return depth

        queue = [(root, 1)]        
        while queue:
            node, level = queue.pop(0)
            depth = max(depth, level)
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append((child, level + 1))
        
        return depth