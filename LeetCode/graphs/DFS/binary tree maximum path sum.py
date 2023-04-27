# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        optimal = float(-inf)

        def dfs(node):
            nonlocal optimal
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)


        
            optimal = max(optimal, left + right + node.val)
            optimal = max(optimal, left + node.val)
            optimal = max(optimal, right + node.val)
            optimal = max(optimal, node.val)

            if max(right, left) < 0:
                return node.val
            
            
            return max(right, left) + node.val
        
        dfs(root)
        
        return optimal
