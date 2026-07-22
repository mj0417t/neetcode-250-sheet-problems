# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res=[]
        def traverse(root):
            if not root:
                return res
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
            return res
        
        return traverse(root)