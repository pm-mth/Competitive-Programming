class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        direction = [(0,1), (0,-1), (1, 0),(-1,0), (1,1),(1,-1),(-1,1),(-1,-1)]
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        
        def dfs(r,c):
            if not inbound(r,c): 
                return
            if board[r][c].isnumeric() or board[r][c] == "B" or board[r][c] == "X":
                return
            if board[r][c] == "E":
                count = 0
                for i, j in direction:
                    nr, nc = r + i, c + j
                    if inbound(nr, nc) and board[nr][nc] == "M":
                        count += 1
                if count:
                    board[r][c] =str(count)
                else:
                    board[r][c] = "B"
                    for i, j in direction:
                        nr = r + i
                        nc = c + j
                        if inbound(nr, nc):
                            dfs(nr,nc)
        dfs(click[0], click[1])  
        return board
