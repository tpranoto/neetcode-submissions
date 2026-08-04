from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for r in range(len(grid)):
            for c in range (len(grid[r])):
                if grid[r][c] == 1:
                    area = self.dfs(grid,r,c)
                    max_area = max(max_area,area)


        return max_area


    
    def dfs(self,grid,r,c) -> int:
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        count = 0
        fringe = []
        fringe.append((r,c))
        grid[r][c] = 0

        while fringe:
            cur_r,cur_c = fringe.pop()
            count+=1

            for dr,dc in dirs:
                new_r,new_c = cur_r+dr,cur_c+dc
                if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c] == 1:
                    fringe.append((new_r,new_c))
                    grid[new_r][new_c] = 0
        
        return count

    def bfs(self,grid,r,c):
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        count = 0
        fringe = deque()
        fringe.append((r,c))

        while fringe:
            cur_r,cur_c = fringe.popleft()
            grid[cur_r][cur_c] = 0
            count+=1

            for dr,dc in dirs:
                new_r,new_c = cur_r+dr,cur_c+dc
                if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c] == 1:
                    fringe.append((new_r,new_c))

        return count


    #     max_area = 0
    #     for x in range(len(grid)):
    #         for y in range(len(grid[0])):
    #             if grid[x][y] == 0:
    #                 continue
    #             max_area = max(max_area,self.dfs(x,y,grid))


    #     return max_area

    # def dfs(self,a,b,grid):
    #     area=0
    #     fringe = []
    #     fringe.append((a,b))

    #     while len(fringe) != 0:
    #         x,y = fringe.pop()
    #         grid[x][y] = 0
    #         area+=1

    #         for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
    #             if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy] != 0 :
    #                 fringe.append((x+dx,y+dy))
    #                 grid[x+dx][y+dy] = 0

    #     return area

    # def bfs(self,a,b,grid):
    #     area= 0
    #     fringe = deque()
    #     fringe.append((a,b))
    #     grid[a][b] = 0

    #     while len(fringe) != 0:
    #         x,y = fringe.popleft()
    #         area+=1

    #         for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
    #             if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy] != 0 :
    #                 fringe.append((x+dx,y+dy))
    #                 grid[x+dx][y+dy] = 0
            
    #     return area

