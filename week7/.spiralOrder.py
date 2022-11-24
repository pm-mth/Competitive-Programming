class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        Left = 0
        Top = 0
        Right = len(matrix[0])
        Bottom = len(matrix)
        
        while Left < Right and Top < Bottom:
            for i in range(Left, Right):
                result.append(matrix[Top][i])
            
            Top += 1
            for i in range(Top, Bottom):
                result.append(matrix[i][Right-1])
            Right -= 1
            
            if not (Left < Right and Top < Bottom):
                break
            for i in range(Right-1, Left-1, -1):
                result.append(matrix[Bottom-1][i]) 
            Bottom -= 1
            for i in range(Bottom-1, Top-1, -1):
                result.append(matrix[i][Left]) 
            Left += 1
        
        return result
        
        
            
        
            
            
                
                
