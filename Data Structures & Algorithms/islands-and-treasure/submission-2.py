from collections import deque

class Solution:
    def __init__(self):
        self.avail = (2**31) - 1
        self.chest = 0
        self.water = -1
        self.dirs = [(0,1),(1,0),(-1,0),(0,-1)]

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == self.chest:
                    q.append((r,c,0))
            
        self.bfs(grid,q)
        

    def bfs(self,grid,q):

        while q:
            r,c,level = q.popleft()

            for dr,dc in self.dirs:
                totr = r+dr
                totc = c+dc

                if 0<=totr<len(grid) and 0<=totc<len(grid[0]) and grid[totr][totc] == self.avail:
                    grid[totr][totc] = min(grid[totr][totc],level+1)
                    q.append((totr,totc,level+1))
