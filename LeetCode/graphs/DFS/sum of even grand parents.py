# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return
            if node.right == None and node.left == None:
                return 

            if node.val % 2 == 0:
                if node.left and node.left.left:
                    count += node.left.left.val
                if node.left and node.left.right:
                    count += node.left.right.val
                if node.right and node.right.left:
                    count += node.right.left.val
                if node.right and node.right.right:
                    count += node.right.right.val
            dfs(node.left)
            dfs(node.right)
            return 
        dfs(root)
        return count
                
