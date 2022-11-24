class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        stack = []
        for item in tasks:
            count[item] += 1
        
        values = [-item for item in count.values()]
        heapq.heapify(values)
#         values.sort()
        time = 0
        
        q = deque()
        
        
        while values or q:
            time += 1
            
            if values:
                v = 1 + heapq.heappop(values)
#                 v = 1 + values[0]
#                 del values[0]
                
                if v:
                    q.append([v, time + n])
                
            if q and q[0][1] == time:
                heapq.heappush(values, q.popleft()[0])
#               values.append(q.popleft()[0])        
        return time
        
