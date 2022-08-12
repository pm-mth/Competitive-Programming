class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:     
        left, right = max(weights), sum(weights)
        answer = right
        while left <= right:
            mid = left + (right - left)//2
            
            if self.count(weights, mid) <= days:
                answer = min(answer, mid)
                right = mid - 1
            else:
                left = mid + 1
        return answer
#     optimizing days for a given weight
    def count(self, weights, val):
        _count = 0
        total = 0
        for w in weights:
            total += w
            if total > val:
                total = w
                _count += 1
        return _count + 1
