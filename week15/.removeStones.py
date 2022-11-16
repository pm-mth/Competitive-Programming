class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        row, col = defaultdict(list), defaultdict(list)
        
        for s, (r,c) in enumerate(stones):
            row[r].append(s)
            col[c].append(s)
            
        visited, n  = set(), len(stones)
        
        def dfs(s):
            if s in visited:
                return 0
            visited.add(s)
            r,c = stones[s]
            
            for ss in chain(row[r], col[c]):
                
                dfs(ss)
            return 1
        res = sum(dfs(s) for s in range(n))
        
        return n - res
        
