class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        smallestPairs = []
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

        while heap:
            add, i, j = heapq.heappop(heap)
            smallestPairs.append((nums1[i], nums2[j]))
            if len(smallestPairs) == k:
                break

            if i == 0 and j < len(nums2) - 1:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            if i < len(nums1) - 1:
                heapq.heappush(heap, (nums1[i + 1] +  nums2[j], i + 1, j))
        
        return smallestPairs
