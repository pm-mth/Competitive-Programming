# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, inter):
            nonlocal ans
            if not node.left and not node.right:
                inter.append(str(node.val))
                num = int("".join(inter))
                ans += num
                inter.pop()
                return

            inter.append(str(node.val))
            if node.left:
                dfs(node.left, inter)
            if node.right:
                dfs(node.right, inter)
            
            inter.pop()
        dfs(root, [])
        return ans

