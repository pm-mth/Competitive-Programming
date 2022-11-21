class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        q = collections.deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
      
        while q:
            (r, c, steps) = q.popleft()
            
            if r == 0 or r == m-1 or c == 0 or c == n-1:
                if steps >0:
                    return steps
           
            for dirc in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                nr = r + dirc[0]
                nc = c + dirc[1]
                
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    q.append((nr,nc,steps+1))
                    maze[nr][nc] = "+"
        return -1
                
        
#         def dfs(r, c):
            
#             if r < 0 or c < 0  or r >= m or c >= n and maze[r][c] == "+":
#                 return 0
#             if 0 <= r < m and 0 <= c < n and maze[r][c] == '-':
#                 maze[r][c] = '+' # V is for visited
#             if r == 0 or c == 0 or r == m- 1 or c == n-1:
#                 return 1
#             count = 1
#             for dirc in ([1, 0], [0, 1], [-1, 0], [0, -1]):
#                 nr = r + dirc[0]
#                 nc = c + dirc[1]
#                 count += min(count, dfs(nr, nc)) 
#             return count
#         if entrance[1] == 0:
#             maze[entrance[0]][entrance[1]] = 'V'
#             return dfs(entrance[0], entrance[1]+1)
            
