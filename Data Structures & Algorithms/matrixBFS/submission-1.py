class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        queue = deque()
        queue.append(((0,0),0))

        visited = set()
        visited.add((0,0))

        while len(queue) > 0:
            current,depth = queue.popleft()
            print(current)
            if current == (len(grid)-1,len(grid[len(grid)-1])-1):
                return depth
            
            for path in self.available_path(current,grid):
                if path in visited:
                    continue
                if path[0] < 0 or path[0] >= len(grid) or path[1] < 0 or path[1] >= len(grid[len(grid)-1]):
                    continue
                if grid[path[0]][path[1]] == 1:
                    continue
                queue.append((path,depth+1))
                visited.add(path)            

        return -1 
    
    def available_path(self, current: Tuple(int,int), grid: List[List[int]] ):
        result = []
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            next_path = (current[0]+x,current[1]+y)
            result.append(next_path)
        return result        
