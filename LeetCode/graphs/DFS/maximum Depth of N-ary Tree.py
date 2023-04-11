
class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if root == None:
            return 0
        max_val = 0
        for node in root.children:
            max_val = max(max_val, self.maxDepth(node))
        
        return max_val + 1
