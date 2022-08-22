class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        direction = [(1,0), (0,1), (0, -1), (-1, 0)]
        n = len(grid)
        def weightedBFS(row, col, destination, direction):
            visited = set()
            
            heap = [(grid[0][0], (row, col))]
            
            while heap:
                t, current = heapq.heappop(heap)
                
                if current == destination:
                    return t
                
                for neighbour in direction:
                    nr = current[0] + neighbour[0]
                    nc = current[1] + neighbour[1]
                    
                    if (nr, nc) not in visited and (nr >= 0) and (nc >= 0) and (nr < n) and (nc < n):
                        heapq.heappush(heap, (max(t, grid[nr][nc]), (nr, nc)))
                        visited.add((nr, nc))
        
        return weightedBFS(0,0, (n-1, n-1), direction)
                
                    
        
