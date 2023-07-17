# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node):
            if not node:
                return (0,0)
            if node in memo:
                return memo[node]
            withrootL, withoutrootL = dfs(node.left)
            withrootR, withoutrootR = dfs(node.right)

            withroot = withoutrootL + withoutrootR + node.val
            withoutroot = max(withrootL, withoutrootL) + max(withrootR, withoutrootR)
            # withoutroot = max(withrootL + withrootR, withoutrootL + withoutrootR,
            # withoutrootR + withrootL, withoutrootL + withrootR)
            memo[node] = (withroot, withoutroot)

            return memo[node]
        
        return max(dfs(root))

        
