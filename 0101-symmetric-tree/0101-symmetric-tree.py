# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def check(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2:
                return False
            if not node2 and node1:
                return False
            
            
            left = check(node1.left, node2.right)
            right = check(node1.right, node2.left)
            
            if node1.val != node2.val:
                return False
            
            return left and right
        
        return check(root.left, root.right)    
            
        
        