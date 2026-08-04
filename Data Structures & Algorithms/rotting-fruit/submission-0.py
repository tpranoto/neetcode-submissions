from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        FRESH,ROTTEN = 1,2
        visited = set()
        fringe = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        fresh_count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == ROTTEN:
                    fringe.append((row,col,0))
                if grid[row][col] == FRESH:
                    fresh_count +=1

        if fresh_count == 0:
            return 0
        
        max_minute = 0
        while len(fringe) != 0:
            row,col,time = fringe.popleft()
            max_minute = max(max_minute,time)

            for dr,dc in directions:
                if 0<=row+dr<len(grid) and 0<=col+dc<len(grid[0]) and grid[row+dr][col+dc] == FRESH:
                    fringe.append((row+dr,col+dc,time+1))
                    grid[row+dr][col+dc] = ROTTEN
                    fresh_count -=1

        if fresh_count >0:
            return -1
        
        return max_minute