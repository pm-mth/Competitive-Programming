class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        dis = sys.maxsize
        index = 0
        for i in range(len(points)):
            if points[i][0] == x:
                if points[i][1] == y:
                    return i 
                if abs(y - points[i][1]) < dis:
                    dis = abs(y - points[i][1])
                    index = i
            elif points[i][1] == y:
                if abs(x - points[i][0]) < dis:
                    dis = abs(x - points[i][0])
                    index = i
        if dis == sys.maxsize:
            return -1
        return index
                
        