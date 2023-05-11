class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for to, fro in richer:
            graph[fro].append(to)
            indegree[to] += 1
            
            
        answer = [i for i in range(len(quiet))]
        visited = set()

        def dfs(node):
            if node in visited:
                return answer[node]
            if graph[node] == []:
                visited.add(node)
                return answer[node]
            for neighbour in graph[node]:
                min_node = dfs(neighbour)
                if quiet[min_node] < quiet[answer[node]]:
                    answer[node] = min_node
            visited.add(node)
            return answer[node]

            
        for i in range(len(quiet)):
            if indegree[i] == 0 and i not in visited:
                dfs(i)
            
        return answer
        

        
