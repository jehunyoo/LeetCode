# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = ""
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                tree += str(node.val) + ','
                queue.append(node.left)
                queue.append(node.right)
            else:
                tree += 'null,'
    
        return tree[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split(',')
        if tree[0] == 'null':
            return None

        node = root = TreeNode(int(tree.pop(0)))
        queue = [root]
        
        while tree:
            node = queue.pop(0)
            if tree[0] != "null":
                node.left = TreeNode(int(tree.pop(0)))
            else:
                tree.pop(0)
            
            if tree[0] != "null":
                node.right = TreeNode(int(tree.pop(0)))
            else:
                tree.pop(0)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
 
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))