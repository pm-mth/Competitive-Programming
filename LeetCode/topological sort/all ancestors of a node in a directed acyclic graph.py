class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        answer = [[] for _ in range(n)]
        for fro, to in edges:
            graph[fro].append(to)
            indegree[to] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            answer[node] = sorted(set(answer[node]))
            for neighbour in graph[node]:
                answer[neighbour].append(node)
                answer[neighbour] += answer[node]
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return answer
