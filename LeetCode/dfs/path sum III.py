# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0

        def dfs(node, pre, store):
            nonlocal res
            if not node:
                return 
            
            
            
            val = pre + node.val
            check = val - targetSum
        
            if check in store:
                res += store[check]

            store[val] += 1
            dfs(node.right,val, store)
            dfs(node.left, val, store)
            store[val] -= 1
            

            return 
        
        store = defaultdict(int)
        store[0] += 1
        dfs(root, 0, store)

        return res
        
            
            
            
            
            
        
