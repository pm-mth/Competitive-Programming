class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = defaultdict(list)
        for num in nums:
            count = 1
            if heap[num -1]:
                count += heapq.heappop(heap[num-1])
            heapq.heappush(heap[num], count)
        
        for val in heap.values():
            if val and val[0] < 3:
                return False
        
        return True
        
