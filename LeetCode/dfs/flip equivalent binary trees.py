# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1:
            return False
        if not root2:
            return False
        if root1.val != root2.val:
            return False
        

        def dfs(x, y):
            if not x and not y:
                return True
            if not x:
                return False
            if not y:
                return False
            
            if not x.left:
                left = None
            if not x.right:
                right = None
            
            if x.left:
                left = x.left.val
            if x.right:
                right = x.right.val

            xchild = [left, right]
            if not y.left:
                left = None
            if not y.right:
                right = None
            
            if y.left:
                left = y.left.val
            if y.right:
                right = y.right.val
            ychild = [left, right]
           

            if xchild[0] == ychild[0] and xchild[1] == ychild[1]:
                return dfs(x.left, y.left) and dfs(x.right, y.right) 
            
            elif xchild[1] == ychild[0] and xchild[0] == ychild[1]:
                x.left, x.right = x.right, x.left
                return dfs(x.left, y.left) and dfs(x.right, y.right)
            else:
                return False
        
        return dfs(root1, root2)


        
