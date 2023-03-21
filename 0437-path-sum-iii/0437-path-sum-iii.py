# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.answer = 0
        self.targetSum = targetSum
        count = defaultdict(int)
        count[0] = 1
        self.findPath(root, 0, count)

        return self.answer
        
    
    def findPath(self, root, prefix, count):     
        if not root:
            return
        prefix += root.val
        if prefix - self.targetSum in count:
            self.answer += count[prefix - self.targetSum]
        
        
        count[prefix] += 1
        self.findPath(root.left, prefix, count)
        self.findPath(root.right, prefix, count)
        count[prefix] -= 1
        
        
        
        
        
        