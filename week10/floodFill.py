class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        
        def fill(r, c):
            nonlocal original
            if r >= len(image) or r < 0 or c >= len(image[0]) or c < 0:
                return 
            
            if image[r][c] != original:
                return
            
            image[r][c] = color
            
            fill(r, c + 1)   #right
            fill(r, c - 1)   #left
            fill(r + 1, c)   #up
            fill(r - 1, c)   #down
            
        fill(sr, sc)
        
        return image
