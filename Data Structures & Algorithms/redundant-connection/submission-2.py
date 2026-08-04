from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()

            if self.dfs(u,visited,-1,adj):
                return [u,v]


        return []

    
    def dfs(self,n,visited,parent,adj):
        visited.add(n)

        for node in adj[n]:
            if node == parent:
                continue
            if node in visited:
                return True
            if self.dfs(node,visited,n,adj):
                return True

        return False
        