class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph  = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        distance = {node:float(inf) for node in range(1, n + 1)}
        distance[k]  = 0
        visited = set()
        priority_queue = [(0, k)]

        while priority_queue:
            dist, node = heapq.heappop(priority_queue)
            if node in visited:
                continue

            visited.add(node)
            for neighbour, weight in graph[node]:
                if dist + weight < distance[neighbour]:
                    distance[neighbour] = dist + weight
                    heapq.heappush(priority_queue, (distance[neighbour], neighbour))
        
        max_ = max(distance.values())
        if max_ == float(inf):
            return -1
    
        return max_

                




        
        
        
