# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        def find (root):
            nonlocal total
            if not root:
                return 
            if root.left == None and root.right == None:
                return 
            find(root.left)
            find(root.right)
            if root.val%2 ==0:
                if root.left and root.left.left:
                    total +=  root.left.left.val
                if root.left and root.left.right:
                    total +=  root.left.right.val
                if root.right and root.right.left:
                    total +=  root.right.left.val
                if root.right and root.right.right:
                    total +=  root.right.right.val
            return
        find(root)
        return total
        
            
