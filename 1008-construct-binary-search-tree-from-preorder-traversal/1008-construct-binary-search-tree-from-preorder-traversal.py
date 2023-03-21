# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.index = 0
        
        return self.findPlace(-inf, inf)
   
    
    def findPlace(self, minval, maxval):
        if self.index >= len(self.preorder):
            return None
        if self.preorder[self.index] <= minval or self.preorder[self.index] >= maxval:
            return None
        
        node = TreeNode()
        node.val = self.preorder[self.index] 
        self.index += 1
        node.left = self.findPlace(minval, node.val)
        node.right = self.findPlace(node.val, maxval)
        
        return node
        
        
        