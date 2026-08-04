class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.dfs((0,0),set((0,0)),grid)
        

    def dfs(
        self,
        current_loc: Tuple(int,int), 
        visited: set[Tuple(int,int)], 
        grid: List[List[int]],
    ) -> int:
        x_max = len(grid)-1
        y_max = len(grid[len(grid)-1])-1
        if current_loc[0] > x_max or current_loc[0] < 0 or current_loc[1] > y_max or current_loc[1] < 0:
            return 0
        if grid[current_loc[0]][current_loc[1]] == 1:
            return 0
        if current_loc == (x_max,y_max):
            return 1
        
        count = 0
        for path in self.available_path(current_loc,visited,grid):
            visited.add(current_loc)
            count += self.dfs(path,visited,grid)
            visited.remove(current_loc)

        return count
    
    def available_path(
        self,
        current_loc: Tuple(int,int),
        visited: set[Tuple(int,int)], 
        grid: List[List[int]],
    ) -> List(Tuple(int,int)):
        result = []
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            n = (current_loc[0]+x,current_loc[1]+y)
            if n in visited:
                continue
            result.append(n)

        return result

