class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
   
        heap = [-num for num in piles]
        heapq.heapify(heap)
        while k > 0:
            num = -heapq.heappop(heap)

            ans = ceil(num/2)
            heapq.heappush(heap, -ans)
            k -= 1
        return -sum(heap)

        
