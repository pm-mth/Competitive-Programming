# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        answer = None
        
        
        def commonAncestor(root, p, q):
            nonlocal answer
            if not root:
                return False
            
            left = commonAncestor(root.left, p, q)
            right = commonAncestor(root.right, p, q)
            

            
            if root.val == q.val or root.val == p.val:
                if left or right:
                    answer = root
                return True
                   
            else:
                if left and right:
                    answer = root
                    return False
                elif left or right:
                    return True
                else:
                    return False
            
                
        commonAncestor(root, p, q)
        
        return answer
                
        