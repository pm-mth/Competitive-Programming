# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        count = defaultdict(int)
        max_element = {}
        def findMode(node):
            if not node:
                return 
            
            findMode(node.left)
            count[node.val] += 1
            findMode(node.right)
        findMode(root)
        
        
        
        answer = sorted(count.items(), key = lambda x:x[1], reverse = True)
        count = dict(answer)
        answer = []
        for key in count.keys():
            if not answer:
                answer.append(key)
            else:
                if count[key] == count[answer[-1]]:
                    answer.append(key)
                else:
                    break
        return answer
        
        return answer
            
    
    
    
            
        