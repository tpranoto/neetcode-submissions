from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    continue
                max_area = max(max_area,self.bfs(x,y,grid))


        return max_area

    def bfs(self,a,b,grid):
        area= 0
        fringe = deque()
        fringe.append((a,b))
        grid[a][b] = 0

        # [0,1,1,0,1],
        # [1,0,1,0,1],
        # [0,1,1,0,1],
        # [0,1,0,0,1]

        while len(fringe) != 0:
            x,y = fringe.popleft()
            area+=1

            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy] != 0 :
                    fringe.append((x+dx,y+dy))
                    grid[x+dx][y+dy] = 0
            
        return area

