class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = defaultdict(int)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
      
        
        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        
        while queue:
            level = queue.copy()
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbour in graph[node]:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        queue.append(neighbour)
                if not queue:
                    return list(level)
        
