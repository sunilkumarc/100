# https://leetcode.com/problems/island-perimeter/description/

class Solution(object):
    rows = 0
    cols = 0
    perimeter = 0
    
    def calculate(self, grid, i, j):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or grid[i][j] != 1:
            return
        
        if j-1 >= 0 and grid[i][j-1] == 0:
            self.perimeter += 1
        if j+1 < self.cols and grid[i][j+1] == 0:
            self.perimeter += 1
        if i-1 >= 0 and grid[i-1][j] == 0:
            self.perimeter += 1
        if i+1 < self.rows and grid[i+1][j] == 0:
            self.perimeter += 1
        
        if i == 0:
            self.perimeter += 1
        if i == self.rows-1:
            self.perimeter += 1
        if j == 0:
            self.perimeter += 1
        if j == self.cols-1:
            self.perimeter += 1
        
        grid[i][j] = 2
        self.calculate(grid, i-1, j)
        self.calculate(grid, i+1, j)
        self.calculate(grid, i, j-1)
        self.calculate(grid, i, j+1)
        
    
    def islandPerimeter(self, grid):
        self.rows = len(grid)
        if self.rows > 0:
            self.cols = len(grid[0])
        
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    self.calculate(grid, i, j)
        
        return self.perimeter