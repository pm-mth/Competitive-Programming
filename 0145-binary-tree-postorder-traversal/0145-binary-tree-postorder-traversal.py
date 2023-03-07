# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        
        def postOrderTraversal(root):
            if not root:
                return
            
            postOrderTraversal(root.left)
            postOrderTraversal(root.right)
            answer.append(root.val)
            
            return answer
        
        return postOrderTraversal(root)
            
        