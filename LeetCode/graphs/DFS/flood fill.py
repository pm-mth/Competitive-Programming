class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        boundary = image[sr][sc]
        if boundary == color:
            return image
            
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def inbound(r, c):
            return 0 <= r < len(image) and 0 <= c < len(image[0])
        
        def dfs(r, c):
            if not inbound(r,c):
                return

            if image[r][c] != boundary:
                return

            image[r][c] = color
            for nr, nc in direction:
                new_r = r + nr
                new_c = c + nc
                dfs(new_r, new_c)
            
        dfs(sr, sc)
        return image
