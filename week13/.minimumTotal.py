class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        #top-down dp
        for i in range(1, n):
            triangle[i][i] += triangle[i-1][i-1]
            triangle[i][0] += triangle[i-1][0]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])
        
        
#         dp = defaultdict(int)
#         n = len(triangle)
#         def dfs(tri):
#             i, j = tri[0], tri[1]
#             if dp[(i,j)]:
#                 return dp[(i, j)]
#             if i == n -1:
#                 return triangle[i][j]
#             if j < len(triangle[i]):
#                 dp[(i,j)] = triangle[i][j] + min(dfs((i+1, j)), dfs((i+1, j+1)))
#             return dp[(i,j)]
#         return dfs((0,0))
        
