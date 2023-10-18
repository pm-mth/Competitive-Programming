# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        coins = defaultdict(int)

        def dfs(node):
            if not node.left and not node.right:
                if node.val > 0:
                    coins[node] = node.val - 1
                    return (node.val - 1, True)
                else:
                    coins[node] = 1
                    return (1, False)
            
            valL, valR, isL, isR = 0,0, False, False
            if node.left:
                valL, isL = dfs(node.left)
            if node.right:
                valR, isR = dfs(node.right)
            
            if isL and isR:
                diff = valL + valR + node.val
                coins[node] = diff - 1
                if diff > 0:
                    return (diff - 1, True)
                coins[node] = -1*diff + 1
                return (-1*diff + 1, False)

            
            if isL:
                diff = valL - valR + node.val
                if diff > 0:
                    coins[node] = diff - 1
                    return (diff - 1, True)
                coins[node] = -1*diff + 1
                
                return (-1*diff + 1, False)
            
            if isR:
                diff = valR - valL + node.val
                if diff > 0:
                    coins[node] = diff - 1
                    return (coins[node], True)
                coins[node] = -1*diff + 1
                
                return (-1*diff + 1 , False)
            
            diff = node.val - valR - valL 
            if diff > 0:
                coins[node] = diff - 1
                return (coins[node], True)
            coins[node] = -1*diff + 1
            
            return (-1*diff + 1, False)
        
        dfs(root)
       
        return sum(coins.values())

            
            

            
                

        
