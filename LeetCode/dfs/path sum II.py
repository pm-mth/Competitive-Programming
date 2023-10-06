# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, ans):
            if not node:
                return 
                
            if not node.right and not node.left:
                if sum(ans) + node.val == targetSum:
                    ans.append(node.val)
                    res.append(ans.copy())
                    ans.pop()
                return
            
            ans.append(node.val)
            if node.right:
                dfs(node.right, ans)
            if node.left:
                dfs(node.left, ans)
            ans.pop()

            return 
        
        dfs(root, [])
        return res
        
           
