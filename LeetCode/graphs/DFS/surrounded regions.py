class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        directions = [(0, 1), (1,0), (-1, 0), (0,-1)]
        
        def surround(r, c):
            return (r == 0 or r == n - 1 ) or (c == 0 or c == m - 1)
        
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m
        
        
        def find(r, c):
            nonlocal border
            if board[r][c] == "X":
                return       
            
            for i, j in directions:
                nr, nc = i + r, j + c
                if inbound(nr, nc) and board[nr][nc] == "O" and (nr,nc) not in border:
                    border.add((nr, nc))
                    find(nr, nc)
            
            return 
        def dfs(r, c):
            nonlocal border
            if board[r][c] == "X":
                return 
            if (r, c) in border:
                return 
            board[r][c] = "X"
            
            for i, j in directions:
                nr, nc = i + r, j + c
                if inbound(nr, nc) and board[nr][nc] == "O" and (nr, nc) not in border:
                    dfs(nr, nc)
            
        border = set()
        for r in range(n):
            for c in range(m):
                if surround(r, c) and board[r][c] == "O" and (r, c) not in border:
                    border.add((r,c))
                    find(r, c)
    
        for r in range(n):
            for c in range(m):
                if (r, c) not in border and not surround(r, c) and board[r][c] == "O" :
                    dfs(r, c)
        
        
        
        
            
        
