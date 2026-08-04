from collections import OrderedDict

class DoublyListNode:
    def __init__(self, key=0, val=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        value = self.cache[key]
        self.cache.pop(key)
        self.cache[key] = value

        return value

    def put(self, key, val):
        if key in self.cache:
            self.cache.pop(key)
        elif self.cap <= len(self.cache):
            self.cache.popitem(last=False)

        self.cache[key] = val
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