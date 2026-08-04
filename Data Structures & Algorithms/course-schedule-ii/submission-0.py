from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for p in prerequisites:
            prereq[p[0]].append(p[1])
        
        visited = set()
        instack = set()
        output = []

        for n in range(numCourses):
            if self.dfs(n,visited,instack,prereq,output):
                return []
        
        return output

    def dfs(self,n:int,visited,instack,prereq,output):
        if n in instack:
            return True
        if n in visited:
            return False
        
        visited.add(n)
        instack.add(n)

        for p in prereq[n]:
            if self.dfs(p,visited,instack,prereq,output):
                return True

        output.append(n)
        instack.remove(n)

        return False