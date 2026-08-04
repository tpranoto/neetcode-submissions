from collections import deque

EMPTY = 0
FRESH = 1
ROTTEN = 2

DIRS = [(1,0),(0,1),(-1,0),(0,-1)]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_o = 0
        rotten_o = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == FRESH:
                    fresh_o+=1
                if grid[row][col] == ROTTEN:
                    rotten_o.append((row,col,0))

        mnts,o_changed = self.bfs(grid,rotten_o)
        
        if fresh_o - o_changed ==0:
            return mnts
        return -1

    def bfs(self,grid,starter:list):
        q = deque(starter)
        for dt in starter:
            grid[dt[0]][dt[1]] = EMPTY
        o_changed = 0
        mnts = 0
        while q:
            curr,curc,mnt = q.popleft()
            
            for dr,dc in DIRS:
                totr = curr+dr
                totc = curc+dc

                if 0<=totr<len(grid) and 0<=totc<len(grid[0]) and grid[totr][totc] == FRESH:
                    q.append((totr,totc,mnt+1))
                    mnts = max(mnts, mnt+1)
                    grid[totr][totc] = EMPTY
                    o_changed+=1
        return mnts, o_changed


    def dfs(self,grid,row,col):
        stack = []
        stack.append((row,col))
        grid[row][col] = EMPTY

        o_changed = 0

        while stack:
            curr,curc = stack.pop()

            for dr,dc in DIRS:
                totr = curr+dr
                totc = curc+dc

                if 0<=totr<len(grid) and 0<=totc<len(grid[0]) and grid[totr][totc] == FRESH:
                    stack.append((totr,totc))
                    grid[totr][totc] = ROTTEN
                    o_changed+=1

        return o_changed




        





        
        # FRESH,ROTTEN = 1,2
        # visited = set()
        # fringe = deque()
        # directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # fresh_count = 0

        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == ROTTEN:
        #             fringe.append((row,col,0))
        #         if grid[row][col] == FRESH:
        #             fresh_count +=1

        # if fresh_count == 0:
        #     return 0
        
        # max_minute = 0
        # while len(fringe) != 0:
        #     row,col,time = fringe.popleft()
        #     max_minute = max(max_minute,time)

        #     for dr,dc in directions:
        #         if 0<=row+dr<len(grid) and 0<=col+dc<len(grid[0]) and grid[row+dr][col+dc] == FRESH:
        #             fringe.append((row+dr,col+dc,time+1))
        #             grid[row+dr][col+dc] = ROTTEN
        #             fresh_count -=1

        # if fresh_count >0:
        #     return -1
        
        # return max_minute