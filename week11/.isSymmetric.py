# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        answer = []
        q = collections.deque()
        q.append(root)
        while q:
            qlen =len(q)
            length = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    if node.left:
                        length.append(node.left.val)
                        q.append(node.left)
                    else:
                        length.append(None)
                    if node.right:
                        length.append(node.right.val)
                        q.append(node.right)
                    else:
                        length.append(None)
            if length:
                n = len(length)
                left = length[:(n//2)]
                right = length[(n//2):]
                res = True
                for i in range (n//2):
                    if left[i] == right[n//2 - 1 - i]:
                        res = True and res
                    else:
                        res = False
                answer.append(res)
        if False in answer:
            return False
        else:
            return True
