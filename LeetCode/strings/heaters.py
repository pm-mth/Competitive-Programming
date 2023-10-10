class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        heaters.sort()
        for num in houses:
            i = bisect_left(heaters, num)
            if i == 0:
                inter = heaters[i] - num
            elif i == len(heaters):
                inter = num - heaters[i - 1]
            else:
                inter = min(num - heaters[i - 1], heaters[i] - num)
            res  = max(res, inter)
        
        return res
