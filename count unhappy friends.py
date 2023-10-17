class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        prefer = defaultdict(list)
        for u, v in pairs:
            prefer[u] = preferences[u][:preferences[u].index(v)]
            prefer[v] = preferences[v][:preferences[v].index(u)]
        
        count = 0
   
        for p1 in prefer:
            for p2 in prefer[p1]:
                if p1 in prefer[p2]:
                    count += 1
                    break
        
        return count
            
        
