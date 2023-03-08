# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = root
        stack = []
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left  
            else:
                right = stack.pop()
                ans.append(right.val) 
                cur = right.right
        return ans
                
                