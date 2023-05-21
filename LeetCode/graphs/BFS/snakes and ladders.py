class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        grid = []
        row = len(board)
        visited = set()
        toggle = 1
        for i in range(len(board) - 1, -1,-1):
            if toggle == 1:
                for j in range(len(board)):
                    grid.append(board[i][j])
                toggle = 0
            elif toggle == 0:
                for j in range(len(board) - 1, -1, -1):
                    grid.append(board[i][j])
                toggle = 1
      
        queue = deque([(1,0)])
        visited.add(1)
        while queue:
            for _ in range(len(queue)):
                num, cost = queue.popleft()
                if num == row * row:
                    return cost

                for i in range(num + 1, min(num + 6, row * row) + 1):
                    if i not in visited:
                        if grid[i - 1] != -1:
                            queue.append((grid[i - 1], cost + 1))
                        else:
                            queue.append((i, cost + 1))
                        visited.add(i)
        return -1
        
                   

                
                



            
