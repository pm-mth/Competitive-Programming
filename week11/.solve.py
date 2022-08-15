class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] == "X":
                return 
            if board[r][c] == 'V':
                return
            if 0 <= r< m and 0 <= c < n and board[r][c] == 'O':
                board[r][c] = 'V' # V is for visited
                
           
            for dirc in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                nr = r + dirc[0]
                nc = c + dirc[1]
                dfs(nr, nc)  
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O' and (row in [0, m - 1] or col in [0, n - 1]):
                    dfs(row, col)
                    
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'V':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'
