class Node:
    def __init__(self, key=-1, val=-1,left=None,right=None):
        self.key =key
        self.val =val
        self.left=left
        self.right=right

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_node_map = {}
        self.most_recent = Node()
        self.least_recent = Node()

        self.most_recent.right = self.least_recent
        self.least_recent.left = self.most_recent
    
    def _remove(self,node):
        node.left.right = node.right
        node.right.left = node.left
        return node

    def _add_most_recent(self,node):
        node.right = self.most_recent.right
        node.left = self.most_recent

        self.most_recent.right.left = node
        self.most_recent.right = node
    
    def _remove_least_recent(self):
        n = self._remove(self.least_recent.left)
        return n

    def _update(self,node):
        n = self._remove(node)
        self._add_most_recent(n)

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1
        node = self.key_node_map[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.val = value
            self._update(node)
            return
        elif len(self.key_node_map) == self.cap:
            n = self._remove_least_recent()
            del self.key_node_map[n.key]

        n = Node(key,value)
        self._add_most_recent(n)
        self.key_node_map[key] = n
