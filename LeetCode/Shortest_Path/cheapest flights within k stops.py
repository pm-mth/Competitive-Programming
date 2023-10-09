class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for u,v, w in flights:
            graph[u].append((v, w))
        
        dist = {node: inf for node in range(n)}
        dist[src] = 0
        
        queue = [(0, 0, src)]

        while queue:
            cur_k, cur_w, u = heapq.heappop(queue)

            for v, w in graph[u]:
                weight = cur_w + w
                if weight < dist[v] and cur_k <= k:
                    dist[v] = weight
                    heapq.heappush(queue, (cur_k + 1, weight, v))
        
        return dist[dst] if dist[dst] != inf else -1

        
