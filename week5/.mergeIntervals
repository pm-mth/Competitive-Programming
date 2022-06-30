class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newlist = []
        intervals.sort()
        for i in range(len(intervals)):
            if newlist and newlist[-1][1] >= intervals[i][0]:
                vary =newlist.pop()
                if vary[1] <= intervals[i][1]:
                    newlist.append([vary[0], intervals[i][1]])
                elif vary[1] > intervals[i][1]:    
                    newlist.append([vary[0], vary[1]])
            else:
                newlist.append(intervals[i])
                
        return newlist
