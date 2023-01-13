class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        diagonal_elements = defaultdict(set)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                diagonal_elements[row - col].add(matrix[row][col])
                
        
        for key in diagonal_elements.keys():
            if len(diagonal_elements[key]) > 1:
                return False
            
        return True
        