# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        queue = deque([root])
        level = [root.val]

        while queue:
            add = 0
            count = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    add += node.left.val
                    count += 1
                if node.right:
                    queue.append(node.right)
                    add += node.right.val
                    count += 1
            if count:
                avg = add/count
                level.append(avg)
        return level
                
                


           
            


            




        

        return [4]
