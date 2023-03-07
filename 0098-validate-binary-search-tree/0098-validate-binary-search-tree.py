# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inOrderTraversal(root, answer):
            if not root:
                return 
            
            inOrderTraversal(root.left, answer)
            answer.append(root.val)
            inOrderTraversal(root.right, answer)
            
            return answer
        
        
        answer = inOrderTraversal(root, [])
        maximum = answer[0]
        for i in range(1, len(answer)):
            if answer[i] <= maximum:
                return False
            maximum= max(maximum, answer[i])
      
        return True
        
        
        
#         if not root.right and not root.left:
#             return True
        
#         if not root.left and root.right:
#             if root.val < root.right.val:
#                 right = self.isValidBST(root.right)
#             else:
#                 return False
        
#         elif not root.right and root.left:
#             if root.left.val < root.val:
#                 left = self.isValidBST(root.left)
#             else:
#                 return False
               
#         elif root.left.val < root.val and root.val < root.right.val:
#             left = self.isValidBST(root.left)
#             right = self.isValidBST(root.right)
#         else:
#             return False
        
#         return left and right
        
        
        
        

        