class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) <= len(self.minHeap):
            if self.minHeap and self.minHeap[0] < num:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)
        else:
            if self.maxHeap and self.maxHeap[0] < -num:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
    


        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2
        return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
