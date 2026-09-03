from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)

        for p in prerequisites:
            prereq[p[0]].append(p[1])
        
        visited = set()
        instack = set()

        for n in range(numCourses):
            if self.check_cycle(visited,instack,prereq,n):
                return False
        
        return True



    def check_cycle(self, visited,instack, prereq,n):
        if n in instack:
            return True
        if n in visited:
            return False

        visited.add(n)
        instack.add(n)
        
        for p in prereq[n]:
            if self.check_cycle(visited,instack,prereq,p):
                return True
        
        instack.remove(n)
        return False
