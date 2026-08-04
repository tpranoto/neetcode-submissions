
DIRS=[(-1,0),(1,0),(0,-1),(0,1)]


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_connected = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))] 
        atlantic_connected = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]

        pac = []
        atl = []

        for r in range (len(heights)):
            pac.append((r,0))
            atl.append((r,len(heights[0])-1))
        
        for c in range (len(heights[0])):
            pac.append((0,c))
            atl.append((len(heights)-1,c))
        
        self.dfs(heights,pac,pacific_connected)
        self.dfs(heights,atl,atlantic_connected)

        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if pacific_connected[r][c] and atlantic_connected[r][c]:
                    res.append([r,c])
            
        return res
                


    def dfs(self,heights,stack,ocean):
        
        while stack:
            row,col = stack.pop()
            ocean[row][col] = True

            for dr,dc in DIRS:
                totr = row+dr
                totc = col+dc

                if 0<=totr<len(heights) and 0<=totc<len(heights[0]) and not ocean[totr][totc] and heights[totr][totc] >= heights[row][col]:
                    stack.append((totr,totc))