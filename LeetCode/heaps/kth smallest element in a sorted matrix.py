class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        smallestEle = []
        heapq.heapify(smallestEle)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(smallestEle,-matrix[i][j])
                if len(smallestEle) > k:
                    heapq.heappop(smallestEle)
        
        return -heapq.heappop(smallestEle)
