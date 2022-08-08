class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start, end = 1 , min(time)*totalTrips
        ans = end
        
        while start <= end:
            mid = (end + start)//2
            total = 0
            for num in time:
                total += (mid//num)
            
            if total < totalTrips:
                start = mid + 1
            else:
                end = mid -1
                ans = min(ans, mid) 
        return ans
