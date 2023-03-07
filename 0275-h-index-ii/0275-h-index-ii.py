class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = -1, max(citations) + 1
        
        
        def check(mid):
            count = 0
            for i in range(len(citations)):
                if citations[i] >= mid:
                    count += 1
            return count
        
        while right > left + 1:
            mid = left + (right - left)//2
            
            if check(mid)  >=  mid:
                left = mid
            else:
                right = mid
                
        return left
        
        