class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        queue = deque([(0,0,1)])
        visited = set([(0,0)])

        direction = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]

        def inbound(r, c):
            return 0 <= r < len(grid)  and 0 <= c < len(grid[0])

        n = len(grid)

        while queue:
            r, c, d = queue.popleft()
            if (r, c) == (n-1, n-1):
                return d

            for i, j in direction:
                nr, nc = r + i, c + j
                if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, d + 1))

        return -1
