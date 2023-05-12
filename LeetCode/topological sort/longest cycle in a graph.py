class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
    

        for i in range(len(edges)):
            if edges[i] != -1:
                graph[i].append(edges[i])
                

        colors = [0] * len(edges)
        def dfs(node):
            nonlocal answer
            if colors[node] == 2:
                return 0
            if graph[node] == []:
                return 0

            if colors[node] == 1:
                colors[node] = 2
                return 1
            
            colors[node] = 1
            cycle = 0
            for neighbour in graph[node]:
                cycle = max(cycle, dfs(neighbour))

            if colors[node] == 2:
                answer = max(answer, cycle)
            colors[node] = 2
            if cycle != 0:
                return cycle + 1
            
            return 0
        answer = 0
        for i in range(len(edges)):
            if colors[i] == 0:
                dfs(i)
        if answer == 0:
            return -1
        return answer

    

               
                
