class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def ship_time(capacity):
            day = 0
            count = 0
            for i in range(len(weights)):
                count += weights[i]
                if count == capacity:
                    day += 1
                    count = 0
                elif count > capacity:
                    day += 1
                    count = weights[i]
            if count:
                day += 1
           
            return day
        
        left, right = max(weights) - 1, sum(weights) + 1
        
        while right > left + 1:
            mid = left + (right - left)//2
        
            if ship_time(mid) <= days:
                right = mid
            else:
                left = mid
        
        return right
                
                
            