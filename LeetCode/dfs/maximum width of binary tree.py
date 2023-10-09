# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append([root, 1])
        answer = 0
        
        while queue:    
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur[0]:
                    level.append(cur[1])
                    if cur[0].left:
                        queue.append([cur[0].left, 2*cur[1] - 1])
                    if cur[0].right:
                        queue.append([cur[0].right, 2*cur[1]])
          
            minimum = level[0]
            maximum = level[-1]
            
            answer = max(answer, maximum - minimum + 1)
     
        return answer
                    
                        
                    
            
            
            
        
