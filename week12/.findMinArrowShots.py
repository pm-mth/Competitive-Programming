class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        stack = []
        count = 0
        i = 0
        while i <= len(points) -1:
            l = sys.maxsize
            h = -l
            while i <= len(points) -1 and stack and (stack[-1] - points[i][0]) >= 0:
                l = min(l, points[i][1])
                h = max(h, points[i][0])
                if l < h:
                    break
                i += 1
               
            if i <= len(points) -1:
                count += 1
                stack.append(points[i][1])
                i += 1
        return count
