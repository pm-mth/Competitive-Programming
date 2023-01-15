class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row):
            if matrix[r][-1] >= target:
                for c in range(col):
                    if matrix[r][c] == target:
                        return True
        return False
        
#         left, right = 0, (row*col) -1
#         while left <= right:
#             mid = left + (right - left)//2
            
#             #finding the row and col
#             r = mid//col
#             c = mid%col
            
#             #searching for the target
#             if matrix[r][c] == target:
#                 return True
#             elif matrix[r][c] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return False
            
            
        
#         for r in range(row):
#             if matrix[r][-1] >= target:
#                 start, end = 0, col-1
#                 while start <= end:
                    
#                     mid = (start + end)//2
#                     if matrix[r][mid] == target:
#                         return True
#                     elif matrix[r][mid] > target:
#                         end = mid -1
#                     else:
#                         start = mid + 1
            
#         return False
        
                    
        
   
            