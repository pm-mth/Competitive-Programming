class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        car_fleets = 0
        time = []
        
        for i in range(len(position)):
            time.append((position[i], speed[i]))
        
        time.sort(reverse = True)
        
        for r in range(len(time)):
            t = (target - time[r][0])/time[r][1]
            if stack and stack[-1] >= t:
                continue
            if stack and stack[-1] < t:
                stack.pop()
                car_fleets += 1
            stack.append(t)
            
        if stack:
            car_fleets += 1
        return car_fleets 
    
            
        