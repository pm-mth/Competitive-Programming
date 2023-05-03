class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        queue = deque()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def addToQueue(i, j):
            if grid[i][j] == 0:
                return

            for r, c in direction:
                nr, nc = i + r , j + c
                if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 1:
                    queue.append((nr, nc, 0))
                    visited.add((nr, nc))
                    addToQueue(nr, nc)
            return


        for i in range(len(grid)):
            flag = False
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i, j))
                    addToQueue(i, j)
                    flag = True
                    break
            if flag:
                break
  
        while queue:
            r, c, d = queue.popleft()

            for i, j in direction:
                nr, nc = r + i, c + j
                if inbound(nr, nc) and (nr, nc) not in visited:
                    if grid[nr][nc] == 1:
                        return d
                    queue.append((nr, nc, d + 1))
                    visited.add((nr, nc))
