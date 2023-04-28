class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m , n = len(mat), len(mat[0])
        answer = [[-1]*n for _ in range(m)]
        queue = deque()

        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        direction = [(0,1),(1,0),(-1,0),(0,-1)]


        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    answer[i][j] = 0
        
        while queue:
            r, c , d = queue.popleft()

            for i, j in direction:
                nr, nc = r + i, c + j
                if inbound(nr, nc) and answer[nr][nc] != -1:
                    continue
                if inbound(nr, nc):
                    queue.append((nr, nc, d + 1))
                    if mat[nr][nc] == 0:
                        answer[nr][nc] = 0
                    else:
                        answer[nr][nc] = d + 1
        return answer



        
      
