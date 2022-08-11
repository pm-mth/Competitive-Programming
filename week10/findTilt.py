# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.post(root, self.total)
        
        return self.total
    def post(self, root, total) -> int:
        if root == None:
            return 0
        l_sum = self.post(root.left, self.total)
        r_sum = self.post(root.right, self.total)
        self.total += abs(r_sum - l_sum)
        # print(total)
        return l_sum + r_sum + root.val
        
        
