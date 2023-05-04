class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)
        queue = deque()
        visited = set()

        for i in range(len(routes)):
            routes[i] = set(routes[i])

        for i in range(len(routes)):
            if source in routes[i]:
                queue.append((i, 1))
                visited.add(i)
            for j in range(i + 1, len(routes)):
                inter = routes[i].intersection(routes[j])
                if inter:
                    graph[i].append(j)
                    graph[j].append(i)
        
        while queue:
            bus, d = queue.popleft()
            if target in routes[bus]:
                return d
            for i in graph[bus]:
                if i not in visited:
                    visited.add(i)
                    queue.append((i, d+1))
        return -1

       
       
          

        
