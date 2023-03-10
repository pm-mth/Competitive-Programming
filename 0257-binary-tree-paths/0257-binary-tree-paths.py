# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.answer = []
        self.findPaths(root, [])
        
        return self.answer
        
    def findPaths(self, node, inter):
        inter.append(str(node.val))
        
        if not node.left and not node.right:
            self.answer.append("->".join(inter))
            return 
       
        if node.left:
            self.findPaths(node.left, inter)
            inter.pop()
        if node.right:
            self.findPaths(node.right, inter)
            inter.pop()

        
        
            
            
        
    
    
        