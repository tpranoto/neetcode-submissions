from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        for x in range (len(grid)):
            for y in range (len(grid[0])):
                if grid[x][y] == "0":
                    continue
                num_of_islands +=1
                self.bfs(x,y,grid)

        return num_of_islands

    def bfs(self,x,y,grid: List[List[str]]):
        fringe = deque()
        fringe.append((x,y))
        while len(fringe) > 0:
            curx,cury = fringe.popleft()
            grid[curx][cury] = "0"
            for diffx, diffy in [(-1,0),(1,0),(0,-1),(0,1)]:
                next_x = curx + diffx
                next_y = cury + diffy
                if next_x < 0 or next_x >=len(grid) or next_y < 0 or next_y >=len(grid[0]):
                    continue
                if grid[next_x][next_y] == "0":
                    continue
                fringe.append((next_x,next_y))
        