# from collections import OrderedDict

class DoublyLinkedList:
    def __init__(self,key,value,nxt=None,prev=None):
        self.key = key
        self.value = value
        self.nxt = nxt
        self.prev = prev

class LRUCache:
    def __init__(self,cap):
        self.cap = cap
        self.key_node_pairs = {}

        self.most_recent = DoublyLinkedList(0,0)
        self.least_recent = DoublyLinkedList(0,0,self.most_recent)
        self.most_recent.nxt = self.least_recent

    def _remove_node(self,node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev  

    def _add_most_recent_node(self,node):
        node.nxt = self.most_recent.nxt
        node.prev = self.most_recent
        self.most_recent.nxt.prev = node 
        self.most_recent.nxt = node

    def get(self,key:int):
        if key not in self.key_node_pairs:
            return -1
        node = self.key_node_pairs[key]
        
        self._remove_node(node)
        self._add_most_recent_node(node)
        return node.value
    
    def put(self,key:int,value:int):
        if key in self.key_node_pairs:
            node = self.key_node_pairs[key]
            self._remove_node(node)
        elif len(self.key_node_pairs) >= self.cap:
            to_rm = self.least_recent.prev
            del self.key_node_pairs[to_rm.key]
            self._remove_node(to_rm)
        
        new_node = DoublyLinkedList(key,value)
        self._add_most_recent_node(new_node)
        self.key_node_pairs[key] = new_node


# class DoublyLinkedList:
#     def __init__(self, key,val,prev=None,next=None):
#         self.key = key
#         self.val = val
#         self.prev = prev
#         self.next = next

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.map_key_link = {}
#         self.most_recent = DoublyLinkedList(0,0)
#         self.least_recent = DoublyLinkedList(0,0,self.most_recent)
#         self.most_recent.next = self.least_recent

#     def get(self, key: int) -> int:
#         if key in self.map_key_link:
#             self._remove_from_list(key)
#             node = self.map_key_link[key]
#             self._add_most_recent(node)
#             return node.val
#         return -1

        

#     def put(self, key: int, value: int) -> None:
#         if key in self.map_key_link:
#             self._remove_from_list(key)
        
#         elif self.cap >= len(self.map_key_link):
#             node = self.least_recent.prev
#             del self.map_key_link[node.key]
#             self._remove_from_list(node.key)


#         node = DoublyLinkedList(key,value,self.most_recent.next,self.most_recent)
#         self.map_key_link[key] = node
#         self._add_most_recent(node)
    
#     def _add_most_recent(self,node):
#         self.most_recent.next.prev = node
#         self.most_recent.next = node

#     def _remove_from_list(self,key):
#         if key in self.map_key_link:
#             node = self.map_key_link[key]
#             node.prev.next = node.next
#             node.next.prev = node.prev

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# class DoublyListNode:
#     def __init__(self, key=0, val=0, left=None, right=None):
#         self.key = key
#         self.val = val
#         self.left = left
#         self.right = right


# class LRUCache:
#     def __init__(self, cap):
#         self.cap = cap
#         self.cache = OrderedDict()

#     def get(self, key):
#         if key not in self.cache:
#             return -1

#         value = self.cache[key]
#         self.cache.pop(key)
#         self.cache[key] = value

#         return value

#     def put(self, key, val):
#         if key in self.cache:
#             self.cache.pop(key)
#         elif self.cap <= len(self.cache):
#             self.cache.popitem(last=False)

#         self.cache[key] = val
        
    # def __init__(self, cap):
    #     self.cap = cap
    #     self.cache = {}
    #     self.most_recent_key = DoublyListNode()
    #     self.least_recent_key = DoublyListNode(right=self.most_recent_key)
    #     self.most_recent_key.left = self.least_recent_key

    # def get(self, key):
    #     if key not in self.cache:
    #         return -1
    #     self._remove_node(self.cache[key])
    #     self._insert_most_recent_node(self.cache[key])
    #     return self.cache[key].val

    # def put(self, key, val):
    #     if key in self.cache:
    #         # remove from linked list
    #         self._remove_node(self.cache[key])
    #     elif self.cap <= len(self.cache):
    #         removed_node = self.least_recent_key.right
    #         del self.cache[removed_node.key]
    #         self._remove_node(removed_node)

    #     self.cache[key] = DoublyListNode(key, val)
    #     self._insert_most_recent_node(self.cache[key])

    # def _remove_node(self, node):
    #     node.left.right = node.right
    #     node.right.left = node.left

    # def _insert_most_recent_node(self, node):
    #     node.right = self.most_recent_key
    #     node.left = self.most_recent_key.left
    #     self.most_recent_key.left.right = node
    #     self.most_recent_key.left = node