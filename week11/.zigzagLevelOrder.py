# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        
        q = collections.deque()
        q.append(root)
        count = 0

        while q:
            qlen =len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)          
            if count%2 == 0 and level:
                answer.append(level)
            elif count%2 != 0 and level:
                level.reverse()
                answer.append(level)
            count += 1
        return answer
        
        
