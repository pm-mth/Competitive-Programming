class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        answer = n*m
        left, right = 1, n*m
        while left <= right:
            mid = left + (right - left)//2
            
            if self.count(m,n, mid) < k:
                left = mid + 1
            else:
                answer = min(answer, mid)
                right = mid - 1
        return answer
    
    def count(self,row, col, val):
        _count = 0
        for r in range(1,row+1):
            _count += min(col, val//r)
        return _count
        
                    
