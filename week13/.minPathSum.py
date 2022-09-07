class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        path = [[grid[0][0], (0,0)]]
        heapq.heapify(path)
        visited = set()
        while path:
            cur, pos = heapq.heappop(path)
            if pos == (m-1, n-1):
                return cur
            if pos[1] + 1 < n and (pos[0], pos[1] + 1) not in visited:
                heapq.heappush(path, [cur+grid[pos[0]][pos[1]+1], (pos[0], pos[1]+1)])
                visited.add((pos[0], pos[1]+1))
            if pos[0] + 1 < m and (pos[0] + 1, pos[1]) not in visited:
                heapq.heappush(path, [cur+grid[pos[0]+1][pos[1]], (pos[0]+1, pos[1])])
                visited.add((pos[0]+1, pos[1]))
                
        
