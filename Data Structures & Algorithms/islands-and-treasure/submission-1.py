from collections import deque

class Solution:
    INF = 2147483647
    WATER = -1
    TREASURE = 0
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        fringe = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == self.TREASURE:
                    fringe.append((row,col))
        
        while len(fringe)!=0:
            r,c = fringe.popleft()
            
            for dr,dc in self.directions:
                if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]) and grid[r+dr][c+dc] == self.INF:
                    grid[r+dr][c+dc] = grid[r][c]+1
                    fringe.append((r+dr,c+dc))
        
        
