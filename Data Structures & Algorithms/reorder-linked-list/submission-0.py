# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return

        length = 0
        temp = head
        while temp != None:
            temp = temp.next
            length +=1

        if length <=1:
            return
        
        mid = length //2
        temp = head
        for _ in range(mid-1):
            temp = temp.next

        list2 = self.reverse(temp.next)
        temp.next = None

        head = self.combine(head,list2)


    
    def reverse(self,head):
        new_head = None

        while head!=None:
            prev = head
            head = head.next
            prev.next = new_head
            new_head = prev

        return new_head


    def combine(self, list1,list2):
        l,r = 0,0
        head = temp = ListNode()
        while list1 != None and list2 != None:
            if l <= r:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
                l+=1
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
                r+=1

        while list1 !=None:
            temp.next = list1
            list1 = list1.next
            temp = temp.next

        while list2 !=None:
            temp.next = list2
            list2 = list2.next
            temp = temp.next
        
        return head.next
