from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = defaultdict(list)

        visited=set()
        instack=set()

        for p in prerequisites:
            preq[p[0]].append(p[1])

        for n in range(numCourses):
            if self.dfs(n,preq,visited,instack):
                return False
        
        return True

        
    def dfs(self,n,preq,visited,instack):
        if n in instack:
            return True
        if n in visited:
            return False
        
        visited.add(n)
        instack.add(n)
        
        for p in preq[n]:
            if self.dfs(p,preq,visited,instack):
                return True
        
        instack.remove(n)

        return False