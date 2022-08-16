class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        direction = [(0,1), (0,-1), (1, 0),(-1,0), (1,1),(1,-1),(-1,1),(-1,-1)]
        
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= m or c >= n: 
                return
            if board[r][c].isnumeric() or board[r][c] == "B" or board[r][c] == "X":
                return
            if board[r][c] == "E":
                count = 0
                for dirc in direction:
                    nr, nc = r + dirc[0], c + dirc[1]
                    if nr < 0 or nc < 0 or nr >= m or nc >= n or board[nr][nc] != "M":
                        continue
                    else:
                        count += 1
                if count:
                    board[r][c] =str(count)
                else:
                    board[r][c] = "B"
                    for dirc in direction:
                        nr = r + dirc[0]
                        nc = c + dirc[1]
                        if nr < 0 or nc < 0 or nr >= m or nc >= n:
                            continue
                        dfs(nr,nc)
        dfs(click[0], click[1])  
        return board
