# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        
        def average(root):
            if not root:
                return (0, 0,0)
            
            if not root.left and not root.right:
                return (root.val,  1, 1)
            
            left = average(root.left)
            right = average(root.right)
            
            
            add = left[0] + right[0] + root.val
            divisor = left[1] + right[1] + 1
            
           
            if (add//divisor) == root.val:
                count = left[2] + right[2] + 1
            else:
                count = left[2] + right[2]
            
            return (add, divisor, count)
        
        return average(root)[2]
                
          
                
                
                
        
        
        