from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes_rel = defaultdict(list)

        for e in edges:
            nodes_rel[e[0]].append(e[1])
            nodes_rel[e[1]].append(e[0])

        visited = set()

        if self.dfs(0,visited,-1,nodes_rel):
            return False
        return len(visited) == n

#    0
#    1
#  2 3 4
#  3
    def dfs(self, n, visited, parent,nodes_rel):
        visited.add(n)

        for node in nodes_rel[n]:
            if node == parent:
                continue
            if node in visited:
                return True
            if self.dfs(node,visited,n,nodes_rel):
                return True
        
        return False
        


        

    # def dfs(self,n,visited,instack,nodes_rel):
    #     if n in instack:
    #         return True
    #     if n in visited:
    #         return False

    #     instack.add(n)

    #     for node in nodes_rel[n]:
    #         if self.dfs(node,visited,instack,nodes_rel):
    #             return True
    #     visited.add(n)
    #     instack.remove(n)

    #     return False