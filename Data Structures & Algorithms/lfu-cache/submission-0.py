from collections import defaultdict

class ListNode:
    def __init__(self,key=0,val=0,left=None,right=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.left = left
        self.right = right   

class DoublyLinkedList:
    def __init__(self):
        self.most_r = ListNode()
        self.least_r = ListNode()    
        self.most_r.right = self.least_r
        self.least_r.left = self.most_r
        self.size = 0

    def length(self):
        return self.size

    def remove(self,node):
        node.left.right = node.right
        node.right.left = node.left
        self.size -=1
        return node

    def remove_least_recent(self):
        return self.remove(self.least_r.left)

    def add_most_r(self,node):
        node.right = self.most_r.right
        node.left = self.most_r
        self.most_r.right.left = node
        self.most_r.right = node
        self.size +=1

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_node = {}
        self.freq_node = defaultdict(DoublyLinkedList)
        self.leastFreq = 0

    def fix_counter(self,node):
        frq = node.freq
        self.freq_node[frq].remove(node)

        if self.leastFreq == frq and self.freq_node[frq].size == 0:
            self.leastFreq +=1

        node.freq+=1
        self.freq_node[node.freq].add_most_r(node)

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        
        node = self.key_node[key]
        self.fix_counter(node)

        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            self.fix_counter(node)
            node.val = value
        elif len(self.key_node) >= self.cap:
            node = self.freq_node[self.leastFreq].remove_least_recent()
            del self.key_node[node.key]
        
        new_node = ListNode(key,value)
        self.freq_node[new_node.freq].add_most_r(new_node)
        self.key_node[key] = new_node
        self.leastFreq = 1




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)