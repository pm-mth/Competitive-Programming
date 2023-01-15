class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        
        row, col = len(matrix), len(matrix[0])
        last_r, last_c = 0, 0
        
        spiral_array = []
        visited = set()
        
        r, c = 0, 0
        while (r, c) not in visited:
            if r < 0 or r >= row or c < 0 or c >= col:
                break
            last_r, last_c = r, c
            visited.add((r, c))
            spiral_array.append(matrix[r][c])
            
            #iterate through all the direction
            for dirc in direction:
                while (r >= 0 or r < row or c >= 0 or c < col):
                    r, c = last_r + dirc[0], last_c + dirc[1]
                    #check out of index scenario
                    if r < 0 or r >= row or c < 0 or c >= col :
                        if r < 0:
                            r += 1
                        if r >= row:
                            r -= 1
                        if c < 0:
                            c += 1
                        if c >= col:
                            c -= 1
                        break
                        
                    #skip if the index is already visited
                    if (r, c) in visited:
                        break
                        
                    last_r, last_c = r, c # hold the last index that is added to the answer
                    visited.add((r, c))                
                    spiral_array.append(matrix[r][c])
                    
            #update next iteration direction        
            r, c = last_r, last_c + 1
        return spiral_array
            
        
            
            
            
            
        
        