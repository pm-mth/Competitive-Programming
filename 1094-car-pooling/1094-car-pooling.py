class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        direction = [0] *1002
        for trip in trips:
            direction[trip[1]] += trip[0]
            direction[trip[2]] -= trip[0]
        accumulator = 0
        maxSeat = 0
        for i in range(len(direction)):
            accumulator += direction[i]
            maxSeat = max(maxSeat, accumulator)
       
        return maxSeat <= capacity
        