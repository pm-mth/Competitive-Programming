# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        total = 0
        answer = []
        self.add(root, targetSum, total, answer)
        if True in answer:
            return True
        else: 
            return False
        
     

    def add(self, root, targetSum, total, answer) -> List:
        if root:
            total += root.val
            if total == targetSum and root.left == None and root.right == None:
                answer.append(True)
            else:
                answer.append(False)
            self.add(root.left, targetSum, total, answer)
            self.add(root.right, targetSum, total, answer)
            
            
        
        
            
        
        
        
