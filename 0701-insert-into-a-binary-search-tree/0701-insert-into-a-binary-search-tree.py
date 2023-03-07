# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        node = root
        def insert(node, val):
            
            if node.left == None and val < node.val:
                node.left = TreeNode(val)
                return 
            if node.right == None and val > node.val:
                node.right = TreeNode(val)
                return 
            
            if val > node.val:
                insert(node.right, val)
            elif val < node.val:
                insert(node.left, val)
                
            return 
        
        insert(node, val)
        
        return root