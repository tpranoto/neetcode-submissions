class Node:
    def __init__(self,key=0,val=0,left=None,right=None):
        self.key = key
        self.value = val
        self.left = left
        self.right = right


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_node = {}
        self.most_recent = Node()
        self.least_recent = Node()
        self.most_recent.right = self.least_recent
        self.least_recent.left = self.most_recent      

    def new_add(self, node):
        node.left = self.most_recent
        node.right = self.most_recent.right

        self.most_recent.right.left = node
        self.most_recent.right = node

    def remove(self, node):
        node.left.right = node.right
        node.right.left = node.left    
        return node
 
    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]

        self.remove(node)
        self.new_add(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            self.remove(node)

        elif self.cap == len(self.key_node):
            node = self.remove(self.least_recent.left)
            del self.key_node[node.key]
        
        node = Node(key,value)
        self.key_node[key] = node
        self.new_add(node)
        
        
