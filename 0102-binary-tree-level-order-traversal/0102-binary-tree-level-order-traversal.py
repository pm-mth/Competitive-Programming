# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root])
        answer = []
        
        while queue:
            length = len(queue)
            level = []
            while length > 0:
                inter = queue.popleft()
                
                if inter:
                    level.append(inter.val)
                    queue.append(inter.left)
                    queue.append(inter.right)
                length -= 1
                
            if level:  
                answer.append(level)
        
        return answer
                
            
                
        
        
        