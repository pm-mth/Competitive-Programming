# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = TreeNode(None)
        self.startPoint = TreeNode(None)
        self.endPoint = TreeNode()

        def fix(node):
            if not node:
                return 
            fix(node.left)
            if not (self.prev.val == None) and self.prev.val > node.val:
                if self.startPoint.val == None:
                    self.startPoint = self.prev
                self.endPoint = node
            self.prev = node
            fix(node.right)
        fix(root)    
        self.startPoint.val, self.endPoint.val = self.endPoint.val, self.startPoint.val
        return root
