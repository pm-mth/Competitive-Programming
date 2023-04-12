class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                x = (bombs[i][0] - bombs[j][0])**2 
                y = (bombs[i][1] - bombs[j][1])**2
                dist = (x + y) ** (1/2)
                if bombs[i][2] >= dist:
                    graph[i].append(j)
        if len(graph) == 0:
            return 1

        def dfs(node, visited):
            visited.add(node)
            for v in graph[node]:
                if v not in visited:
                    dfs(v, visited)


        max_val = 0
        for node in range(len(bombs)):
            visited = set()
            dfs(node, visited)
            max_val = max(max_val, len(visited))
        return max_val
