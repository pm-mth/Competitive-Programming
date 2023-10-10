# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        count = {}

        def dfs(node):
            nonlocal count
            if not node:
                return [None]
            
            if not node.left and not node.right:
                if (node.val) in count:
                    count[(node.val)][0] += 1
                else:
                    count[(node.val)] = [1, node]
                return [node.val]

            
            left = dfs(node.left)
            right = dfs(node.right)

            temp = [node.val]
            temp += left + right
            
            ans = tuple(temp)
            if ans in count:
                count[ans][0] += 1
            else:
                count[ans] = [1, node]
            
            return temp
        
        dfs(root)
        res = []
       
        for key in count.keys():
            if count[key][0] > 1:
                res.append(count[key][1])
        return res
            

            
