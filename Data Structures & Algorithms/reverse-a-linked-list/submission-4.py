# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = None

        while head:
            prev = head
            head = head.next
            prev.next = newhead
            newhead = prev
        
        return newhead
