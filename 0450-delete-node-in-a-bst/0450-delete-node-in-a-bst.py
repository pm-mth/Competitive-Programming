# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def minValue(node):
            current = node
            while current.left:
                current = current.left
            return current
        
        
        def delete(node, key):
            if not node:
                return node
            
            if node.val > key:
                node.left = delete(node.left, key)
                
            elif node.val < key:
                node.right = delete(node.right, key)
            
            else:
                if not node.left:
                    return node.right
                    
                if not node.right:
                    return node.left
                
                temp = minValue(node.right)
                
                node.val = temp.val
                
                node.right = delete(node.right, temp.val)
                
            return node
        
        return delete(root, key)
        
                
                
                
            