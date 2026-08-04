# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        reversed = None

        while head != None:
            prev = head
            head = head.next
            prev.next = reversed
            reversed = prev
        
        return reversed
        