"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_new_map = {}
        fringe = deque()
        old_new_map[node] = Node(node.val)
        fringe.append(node)

        while fringe:
            cur = fringe.popleft()

            for nei in cur.neighbors:
                if nei not in old_new_map:
                    old_new_map[nei] = Node(nei.val)
                    fringe.append(nei)
                old_new_map[cur].neighbors.append(old_new_map[nei])
        
        return old_new_map[node]

        # new_nodes_map = {}
        
        # def dfs(node):
        #     if node in new_nodes_map:
        #         return new_nodes_map[node]
            
        #     new_node = Node(node.val)
        #     new_nodes_map[node] = new_node
        #     for n in node.neighbors:
        #         new_node.neighbors.append(dfs(n))

        #     return new_node
        


        return dfs(node)


    

