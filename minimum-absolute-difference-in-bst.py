# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    diff = 100000
    prev = -100000
    
    # inorder traversal, recursion
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root:
            self.getMinimumDifference(root.left)
            self.diff = min(self.diff, root.val - self.prev)
            self.prev = root.val            
            self.getMinimumDifference(root.right)

        return self.diff
    
    # inorder traversal, iteration
    def getMinimumDifference(self, root: TreeNode) -> int:
        diff = 100000 # 0 <= node.val <= 10^5
        prev = -100000
        stack = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            
            diff = min(diff, node.val - prev)
            prev = node.val
            
            node = node.right
        
        return diff