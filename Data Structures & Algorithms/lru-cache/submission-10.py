class Node:
    def __init__(self,key=0,val=0,left=None,right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}
        self.most_recent = Node()
        self.least_recent = Node()

        self.most_recent.right = self.least_recent
        self.least_recent.left = self.most_recent


    def _remove(self,node):
        node.left.right = node.right
        node.right.left = node.left

        
    def _add(self,node):
        node.left = self.most_recent
        node.right = self.most_recent.right

        self.most_recent.right.left = node
        self.most_recent.right = node     


    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        
        # remove from list
        self._remove(node)
        # add back to most recent
        self._add(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
             # remove from list
            self._remove(node)

            node.val = value
            
            # add back to most recent
            self._add(node)
            return

        if len(self.nodes) >= self.cap:
            lr_node = self.least_recent.left
            self._remove(lr_node)
            del self.nodes[lr_node.key]

        node = Node(key,value)
        self._add(node)
        self.nodes[key] = node
        
