class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        like_time = 0
        satisfaction.sort()
        for i in range(len(satisfaction)):
            time = 1
            add = 0
            for j in range(i, len(satisfaction)):
                add += time * satisfaction[j]
                time += 1
            
            like_time = max(like_time, add)
        
        return like_time
        
