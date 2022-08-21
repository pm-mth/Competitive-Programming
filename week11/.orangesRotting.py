class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append([i, j])
                    
                    
        q = collections.deque()
        for rot in rotten:
            q.append(rot)
        
        count = 0
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                for dirc in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                    nr = node[0] + dirc[0]
                    nc = node[1] + dirc[1]
                    if nr >= 0 and nc >= 0 and nr < m and nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr, nc])
            count += 1

            # optimizing for exception
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        if count:
            return count -1
        else:
            return 0
