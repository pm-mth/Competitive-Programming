class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        q = collections.deque()
        q.append(start)
        
        while q:
            qlen =len(q)
            for _ in range(qlen):
                i = q.popleft()
                if arr[i] == 0:
                    return True
                visited.add(i)
                for dirc in [i+ arr[i], i - arr[i]]:
                    if dirc not in visited and dirc >= 0 and dirc < len(arr):
                        if arr[dirc] == 0:
                            return True
                        else:
                            q.append(dirc)
        return False
            
        
