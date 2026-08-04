from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = defaultdict(list)
        for p in prerequisites:
            adj[p[1]].append(p[0])

        prereq = defaultdict(set)
        def dfs(n):
            if n not in prereq:
                for p in adj[n]:
                    for crs in dfs(p):
                        prereq[n].add(crs)
                    prereq[n].add(p)

            return prereq[n]
            
        for n in range(numCourses):
            dfs(n)

        print(prereq)
        res = []
        for u,v in queries:
            if u in prereq[v]:
                res.append(True)
            else:
                res.append(False)

        return res