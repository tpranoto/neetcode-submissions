from collections import deque

class Solution:
    def __init__(self):
        self.land = "1"
        self.water= "0"
        self.dirs = [(1,0),(0,1),(-1,0),(0,-1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == self.land:
                    self.bfs(grid,r,c)
                    num+=1
        
        return num
    
    def dfs(self,grid,r,c):
        stack = []
        stack.append((r,c))
        grid[r][c] = self.water

        while stack:
            curr,curc = stack.pop()

            for dr,dc in self.dirs:
                totr,totc = curr+dr,curc+dc

                if 0<=totr<len(grid) and 0<=totc<len(grid[0]) and grid[totr][totc] == self.land:
                    stack.append((totr,totc))
                    grid[totr][totc] = self.water

    def bfs(self,grid,r,c):
        q = deque()
        q.append((r,c))
        grid[r][c] = self.water

        while q:
            curr,curc = q.popleft()

            for dr,dc in self.dirs:
                totr,totc = curr+dr,curc+dc

                if 0<=totr<len(grid) and 0<=totc<len(grid[0]) and grid[totr][totc] == self.land:
                    q.append((totr,totc))
                    grid[totr][totc] = self.water
