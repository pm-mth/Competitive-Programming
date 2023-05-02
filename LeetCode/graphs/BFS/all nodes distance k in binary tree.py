# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        graph = defaultdict(list)
        graph[-1].append(root.val)
        def addToGraph(parent, node):
            if not node:
                return 
            
            graph[node.val].append(parent)
            if node.left:
                graph[node.val].append(node.left.val)
                addToGraph(node.val, node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                addToGraph(node.val, node.right)
        
        addToGraph(-1, root)


        queue = deque([(target.val, 0)])
        answer = []
        visited = set([target.val])
        while queue:
            node, d = queue.popleft()
            if d == k and node != -1:
                answer.append(node)
            for u in graph[node]:
                if u not in visited:
                    queue.append((u, d + 1))
                    visited.add(u)
        return answer
        
