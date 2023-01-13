class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        
        if r*c != row*col:
            return mat
        
        answer = [[0 for _ in range(c)] for _ in range(r)]
        
   
        for i in range(row*col):
            answer[i//c][i%c] = mat[i//col][i%col]
            
        return answer
        