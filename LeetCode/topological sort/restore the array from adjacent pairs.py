class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = defaultdict(int)

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        answer = []

        def dfs(node):
            nonlocal answer
            for neighbour in graph[node]:
                if neighbour not in visited:
                    answer.append(neighbour)
                    visited.add(neighbour)
                    dfs(neighbour)

        visited = set()
        for node in degree.keys():
            if degree[node] == 1:
                if node not in visited:
                    visited.add(node)
                    answer.append(node)
                    dfs(node)

        return answer
        
       

        
        
        answer = []
        while queue:
            node = queue.popleft()
            



        
