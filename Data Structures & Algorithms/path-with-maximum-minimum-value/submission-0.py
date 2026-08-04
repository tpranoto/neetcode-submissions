import heapq

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])   

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        visited = [[False]*C for _ in range(R)]

        fringe = []
        heapq.heappush(fringe,(-grid[0][0],0,0))
        visited[0][0] = True

        min_ans = grid[0][0]

        while fringe:
            val,row,col = heapq.heappop(fringe)
            min_ans = min(min_ans,-val)
            if row == R-1 and col == C-1:
                break

            for dr,dc in dirs:
                if 0<=row+dr<R and 0 <=col+dc<C and visited[row+dr][col+dc] ==False:
                    heapq.heappush(fringe,(-grid[row+dr][col+dc],row+dr,col+dc))
                    visited[row+dr][col+dc] = True


        return min_ans