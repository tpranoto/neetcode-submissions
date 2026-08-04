from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range (len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid,r,c)
                    islands+=1
        
        return islands


    def bfs(self,grid,r,c):
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        fringe = deque()
        fringe.append((r,c))

        while fringe:
            curr_r,curr_c = fringe.popleft()
            grid[curr_r][curr_c] = "0"

            for dr,dc in dirs:
                new_r,new_c = curr_r+dr,curr_c+dc
                if 0<= new_r < len(grid) and 0<= new_c < len(grid[0]) and grid[new_r][new_c] == "1":
                    fringe.append((new_r,new_c))

    
    def dfs(self,grid,r,c):
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        fringe = []
        fringe.append((r,c))

        while fringe:
            cur_r,cur_c = fringe.pop()
            grid[cur_r][cur_c] = "0"

            for dr,dc in dirs:
                new_r,new_c = cur_r+dr,cur_c+dc

                if 0<=new_r<len(grid) and 0<= new_c < len(grid[0]) and grid[new_r][new_c] == "1":
                    fringe.append((new_r,new_c))
    





    #     num_of_islands = 0
    #     for x in range (len(grid)):
    #         for y in range (len(grid[0])):
    #             if grid[x][y] == "0":
    #                 continue
    #             num_of_islands +=1
    #             self.dfs(x,y,grid)

    #     return num_of_islands

    # def bfs(self,x,y,grid: List[List[str]]):
    #     fringe = deque()
    #     fringe.append((x,y))
    #     while len(fringe) > 0:
    #         curx,cury = fringe.popleft()
    #         grid[curx][cury] = "0"
    #         for diffx, diffy in [(-1,0),(1,0),(0,-1),(0,1)]:
    #             next_x = curx + diffx
    #             next_y = cury + diffy
    #             if next_x < 0 or next_x >=len(grid) or next_y < 0 or next_y >=len(grid[0]):
    #                 continue
    #             if grid[next_x][next_y] == "0":
    #                 continue
    #             fringe.append((next_x,next_y))

    # def dfs(self,x,y,grid):
    #     fringe = []
    #     fringe.append((x,y))
    #     while len(fringe) > 0:
    #         curx,cury = fringe.pop()
    #         grid[curx][cury] = "0"
    #         for diffx, diffy in [(-1,0),(1,0),(0,-1),(0,1)]:
    #             next_x = curx + diffx
    #             next_y = cury + diffy
    #             if next_x < 0 or next_x >=len(grid) or next_y < 0 or next_y >=len(grid[0]):
    #                 continue
    #             if grid[next_x][next_y] == "0":
    #                 continue
    #             fringe.append((next_x,next_y))

