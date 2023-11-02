# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        count =  0

        def solve(node):
            nonlocal count
            if not node:
                return [0, 0]
            
            left = solve(node.left)
            right = solve(node.right)

            add = left[0] + right[0] + node.val
            num = left[1] + right[1] + 1

            if num != 0 and  (add // num) == node.val:
                count += 1
            
            return [add, num]
        
        solve(root)
        return count


        