class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        dist = {node: 0 for node in range(n)}
        dist[start_node] = 1
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        queue = [(-dist[start_node], start_node)]
       
        while queue:
            cur_w, u = heapq.heappop(queue)
            
            for v, w in graph[u]:
                if -cur_w * w > dist[v]:
                    dist[v] = -cur_w * w
                    heapq.heappush(queue, (-dist[v], v))
        return dist[end_node]
