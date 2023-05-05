class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        heap = []
        heapify(heap)
        answer = []

        for key in frequency.keys():
            heapq.heappush(heap, (-frequency[key], key))
        i = 0
        while i < k:
            res = heapq.heappop(heap)
            answer.append(res[1])
            i += 1
        
        return answer
