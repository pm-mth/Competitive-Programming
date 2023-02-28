class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        flight = [0]*n
        for num in bookings:
            flight[num[0]-1] += num[2]
            if num[1] < n:
                flight[num[1]] -= num[2]
                
        for i in range(1, n):
            flight[i] = flight[i-1] + flight[i]
        return flight