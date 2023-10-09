# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        res = None

        def dfs(node):
            nonlocal res
            if not node:
                return False
            

            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.val in (p.val, q.val):
                mid = True
            else:
                mid = False
            
            
            if (mid and left) or (mid and right)  or (left and right):
                res = node
                return False
            
            return left or right or mid
        
        dfs(root)
        return res
            
            
                
        
