class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(y - x))
        

        if len(heap) == 1:
            return -heapq.heappop(heap)
        return 0
        

        
