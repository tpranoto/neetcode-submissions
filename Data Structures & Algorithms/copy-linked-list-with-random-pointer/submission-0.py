"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = Node(0)
        old_new_map = {}
        temp =new_head
        old_temp = head

        while old_temp != None:
            temp.next = Node(old_temp.val)
            old_new_map[old_temp] = temp.next
            temp = temp.next
            old_temp = old_temp.next
        
        temp = new_head.next
        while head !=None:
            rand_val = None
            if head.random in old_new_map:
                rand_val = old_new_map[head.random]
            temp.random = rand_val
            temp = temp.next
            head = head.next

        return new_head.next