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

        new_nodes_map = {}
        
        def dfs(node):
            if node in new_nodes_map:
                return new_nodes_map[node]
            
            new_node = Node(node.val)
            new_nodes_map[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n))

            return new_node
        


        return dfs(node)


    

