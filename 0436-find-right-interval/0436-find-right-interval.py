class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index = defaultdict(int)
        start = []
        
        for i in range(len(intervals)):
            index[intervals[i][0]] = i
            start.append(intervals[i][0])
        
        
        start.sort()
        answer = []
        for i in range(len(intervals)):
            target = intervals[i][1]
            
            left, right = -1, len(start)
            
            while right > left + 1:
                mid = left + (right - left)//2
                
                if start[mid] >= target:
                    right = mid
                else:
                    left = mid
                
            if right == len(intervals):
                answer.append(-1)
            else: 
                answer.append(index[start[right]])
                    
        return answer
                    
                    