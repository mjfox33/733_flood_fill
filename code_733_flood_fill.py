# An image is represented by an m x n integer grid image where image[i][j] 
# represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. 
# You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, 
# plus any pixels connected 4-directionally to the starting pixel 
# of the same color as the starting pixel, plus any pixels connected 
# 4-directionally to those pixels (also with the same color), and so on. 
# Replace the color of all of the aforementioned pixels with newColor.

#Return the modified image after performing the flood fill.

#Constraints:
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], newColor < 216
# 0 <= sr < m
# 0 <= sc < n
class Solution:
    def __init__(self):
        self.visited = set()
        
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        start_color = image[sr][sc]
        self.r_flood_fill(image, sr, sc, newColor, start_color)
        return image

    def r_flood_fill(self, image, sr, sc, new_color, start_color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr]) or image[sr][sc] != start_color:
            return 0
        
        if (sr, sc) in self.visited:
            return 0
        
        self.visited.add((sr, sc))

        image[sr][sc] = new_color
        
        self.r_flood_fill(image, sr-1, sc, new_color, start_color)
        self.r_flood_fill(image, sr+1, sc, new_color, start_color)
        self.r_flood_fill(image, sr, sc-1, new_color, start_color)
        self.r_flood_fill(image, sr, sc+1, new_color, start_color)