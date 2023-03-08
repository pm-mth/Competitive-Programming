# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left , right = float(-inf), float(inf)
        
        
        def validate(l, r, node):
            if not node:
                return True
            
            if node.val <= l or node.val >= r:
                return False
        
            left = validate(l, min(r, node.val), node.left)
            right = validate(max(l, node.val), r, node.right)
  
            
            return left and right
        
        return validate(left,  right, root)
            
            
            
            
        
        #def inOrderTraversal(root, answer):
#             if not root:
#                 return 
            
#             inOrderTraversal(root.left, answer)
#             answer.append(root.val)
#             inOrderTraversal(root.right, answer)
            
#             return answer
        
        
#         answer = inOrderTraversal(root, [])
#         maximum = answer[0]
#         for i in range(1, len(answer)):
#             if answer[i] <= maximum:
#                 return False
#             maximum= max(maximum, answer[i])
      
#         return True
        
        
        
        

        