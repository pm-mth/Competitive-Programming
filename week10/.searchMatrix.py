class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix[0]) - 1
        i = 0
        while start <= end and i < len(matrix):
            mid = (start + end)//2
            
            if matrix[i][end] < target:
                i += 1
            else:
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    end = mid -1
                else:
                    start = mid + 1
                
            
