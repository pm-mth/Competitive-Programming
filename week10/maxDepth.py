"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def findMax(root):
            if not root:
                return 0
            
            if root.children == []:
                return 1
            
            ans = 0
            for child in root.children:
                ans = max(ans, findMax(child))
                
            return ans + 1
        
        return findMax(root)
