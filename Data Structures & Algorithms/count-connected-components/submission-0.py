class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False for i in range(n)]
        adj = [[] for i in range(n)]
        
        for edge1,edge2 in edges:
            adj[edge1].append(edge2)
            adj[edge2].append(edge1)

        def dfs(node):
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        count = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                count+=1
        
        return count
        
