class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        directions = [(0,1),(1, 0), (0,-1),(-1,0)]
        def inbound(r, c):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0])

        queue = deque()
        queue.append((entrance[0], entrance[1],0))
        n, m = len(maze), len(maze[0])
        visited = set([(entrance[0], entrance[1])])
        def maze_exit(r, c):
            if (r == 0 or r == n - 1) or (c == 0 or c == m - 1):
                return True
            return False

        while queue:
            r, c, d = queue.popleft()
          
            if (r, c) != (entrance[0],entrance[1]) and maze_exit(r, c):
                return d
            
            for i, j in directions:
                nr, nc = r + i, c + j
                if inbound(nr, nc) and (nr, nc) not in visited and maze[nr][nc] == ".":
                    queue.append((nr, nc, d + 1))
                    visited.add((nr, nc))
        return -1
        

            
            


