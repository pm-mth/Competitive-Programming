# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        
        def find(root, k):
            if not root:
                return -1
        
            left = find(root.left, self.k)
            
            self.k -= 1
            if self.k == 0:
                return root.val
    
            right = find(root.right, self.k)
        

            return max(right, left)
        return find(root, k)
    
            
            
        
     
        
