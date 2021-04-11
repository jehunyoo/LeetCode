# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # inorder traversal, recursion
    def minDiffInBST(self, root: TreeNode) -> int:
        self.diff = 100000 # 0 <= node.val <= 10^5 or sys.maxsize
        self.prev = -100000 # or -sys.maxsize
        
        def inorder(node=root):
            if node:
                inorder(node.left)
                self.diff = min(self.diff, node.val - self.prev)
                self.prev = node.val            
                inorder(node.right)
        
        inorder()
        return self.diff
    
    # inorder traversal, iteration
    def minDiffInBST(self, root: TreeNode) -> int:
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